import QtQuick 2.0
import QtQuick.Window 2.2

Window {
    id: window
    visible: true
    width: 640
    height: 480
    title: "Touch Test"

    MultiPointTouchArea {
        anchors.fill: parent
        onTouchUpdated: {
            console.log("Touch points:", touchPoints.length)
            for (var i in touchPoints) {
                console.log("Point", i,
                            "- ID:", touchPoints[i].pointId,
                            "X:", touchPoints[i].x,
                            "Y:", touchPoints[i].y)
            }
        }
    }
}

