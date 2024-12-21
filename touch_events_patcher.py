#!/usr/bin/env python3

import evdev
from evdev import InputDevice, UInput, AbsInfo, ecodes as e

# Path to the physical (source) touch device
SOURCE_DEVICE_PATH = "/dev/input/event8"

SIMULATED_TOUCH_EVENT_WIDTH = 100 # in surface units

# Define capabilities for the virtual device
# We include all events we need to forward or emit.
capabilities = {
    # Absolute axes (both single-touch and multi-touch)
    e.EV_ABS: [
        # Single-touch axes
        (e.ABS_X, AbsInfo(0, 0, 32767, 0, 0, 118)),
        (e.ABS_Y, AbsInfo(0, 0, 32767, 0, 0, 210)),

        # Multi-touch axes
        (e.ABS_MT_POSITION_X, AbsInfo(0, 0, 32767, 0, 0, 118)),
        (e.ABS_MT_POSITION_Y, AbsInfo(0, 0, 32767, 0, 0, 210)),
        (e.ABS_MT_TOUCH_MAJOR, AbsInfo(0, 0, 255, 0, 0, 0)),
        (e.ABS_MT_WIDTH_MAJOR, AbsInfo(0, 0, 255, 0, 0, 0)),
        (e.ABS_MT_TRACKING_ID, AbsInfo(0, 0, 65535, 0, 0, 0)),
        (e.ABS_MT_SLOT, AbsInfo(0, 0, 9, 0, 0, 0)),
    ],
    # Key events for BTN_TOUCH
    e.EV_KEY: [
        e.BTN_TOUCH
    ],
    # Misc events for MSC_TIMESTAMP
    e.EV_MSC: [
        e.MSC_TIMESTAMP
    ]
}

def main():
    try:
        # Open the real (physical) touch device
        source_device = InputDevice(SOURCE_DEVICE_PATH)
        print(f"Forwarding events from: {source_device.name} ({SOURCE_DEVICE_PATH})")

        # Create the virtual device with the above capabilities
        virtual_device = UInput(
            events=capabilities,
            name="Virtual Touch Device",
            vendor=0x1,
            product=0x1,
            version=0x1,
            input_props=[e.INPUT_PROP_DIRECT]
        )
        print("Created virtual device: Virtual Touch Device")

        # Read events in a loop
        for event in source_device.read_loop():

            # 1) ABS events (single-touch + multi-touch)
            if event.type == e.EV_ABS:
                if event.code in [
                    e.ABS_X,
                    e.ABS_Y,
                    e.ABS_MT_POSITION_X,
                    e.ABS_MT_POSITION_Y,
                    e.ABS_MT_TRACKING_ID
                ]:
                    # Forward the original event
                    virtual_device.write(event.type, event.code, event.value)

                    # Only when the code == ABS_MT_POSITION_X do we add the missing events
                    if event.code == e.ABS_MT_POSITION_X:
                        virtual_device.write(e.EV_ABS, e.ABS_MT_TOUCH_MAJOR, SIMULATED_TOUCH_EVENT_WIDTH)
                        virtual_device.write(e.EV_ABS, e.ABS_MT_WIDTH_MAJOR, SIMULATED_TOUCH_EVENT_WIDTH)

            # 2) KEY events (BTN_TOUCH)
            elif event.type == e.EV_KEY and event.code == e.BTN_TOUCH:
                virtual_device.write(event.type, event.code, event.value)

            # 3) MSC events (MSC_TIMESTAMP)
            elif event.type == e.EV_MSC and event.code == e.MSC_TIMESTAMP:
                virtual_device.write(event.type, event.code, event.value)
                virtual_device.syn() # Sync after each timestamp we sent

    except KeyboardInterrupt:
        print("Exiting on keyboard interrupt...")
    except OSError as err:
        print(f"OS error: {err}")
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        # Clean up devices
        try:
            virtual_device.close()
        except:
            pass
        try:
            source_device.close()
        except:
            pass

if __name__ == "__main__":
    main()
