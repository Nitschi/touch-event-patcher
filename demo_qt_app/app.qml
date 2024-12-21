import QtQuick 2.0
import QtQuick.Window 2.2

Window {
    id: window
    visible: true
    width: 640
    height: 480
    title: "Touch Test"

    // We'll store the formatted touch data in this property.
    property string touchInfo: ""

    MultiPointTouchArea {
        anchors.fill: parent
        onTouchUpdated: {
            var str = "Touch points: " + touchPoints.length + "\n"
            for (var i in touchPoints) {
                str += "Point " + i +
                       " - ID: " + touchPoints[i].pointId +
                       "  X: " + touchPoints[i].x +
                       "  Y: " + touchPoints[i].y + "\n"
            }
            // Update the text that will be displayed
            window.touchInfo = str
        }
    }

    Text {
        anchors.centerIn: parent
        text: window.touchInfo
        font.pointSize: 14
        wrapMode: Text.WordWrap
        color: "black"
    }
}
