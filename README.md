# Touch Events Patcher
Reads touch events from a touch display device and re-emits them + adds missing events, so Qt handles the touch events correctly.

# Prerequisites
- Python3
- `sudo apt-get install libevdev-dev` 
- `pip install -r requirements.txt`

# Run
Adjust the python file, so touch events are read from the correct device (e.g. /dev/input/event19`)
`./touch_events_patcher.py`
