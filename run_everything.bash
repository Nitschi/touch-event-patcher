#! /bin/bash

export QT_QPA_EGLFS_PHYSICAL_WIDTH=640
export QT_QPA_EGLFS_PHYSICAL_HEIGHT=480
export QT_QPA_EVDEV_TOUCHSCREEN_PARAMETERS=/dev/input/event20

sudo ./touch_events_patcher.py &
qmlscene demo_qt_app/app.qml -platform eglfs
