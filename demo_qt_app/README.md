# Summary
Simple app that logs recognized touch events.
This can reproduce an error with a beetronics touchscreen, where touch-events are not recognized correctly.

# Pre-requisites
```bash
sudo apt update
sudo apt install qtdeclarative-dev-tools qmlscene qml-module-qtquick2 qml-module-qtquick-window2 qml-module-qtquick-controls2 qml-module-qtquick-layouts
```

# Running
`qmlscene app.qml`

# Adjusting the Touch-Device (untested)
`QT_QPA_EVDEV_TOUCHSCREEN_PARAMETERS=/dev/input/eventXY qmlscene myapp.qml -platform eglfs`

