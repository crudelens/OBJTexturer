import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button{
    id: btnTopBar
    implicitWidth: 35
    implicitHeight: 35
    //CUSTOM_PROPERTIES
    property url btnIconSource: "../../images/svg_images/minimize_icon.svg"
    property color colorDefault: "#D96704"
    property color colorMouseOver: "#F29F05"
    property color colorPressed: "#F2B705"
    QtObject{
        id: internal
        property var dynamicColor: if(btnTopBar.down){
                                       btnTopBar.down ? colorPressed : colorDefault
                                   } else {
                                       btnTopBar.hovered ? colorMouseOver : colorDefault
                                   }
    }

    background: Rectangle{
        id:bgBtn
        color: internal.dynamicColor
        Image{
            id:iconBtn
            anchors.verticalCenter: parent.verticalCenter
            source: btnIconSource
            anchors.horizontalCenter: parent.horizontalCenter
            height: 16
            width: 16
            fillMode: Image.PreserveAspectFit
            visible: false

        }

        ColorOverlay{
            anchors.fill: iconBtn
            source: iconBtn
            color: "#ffffff"
            antialiasing: false
        }
      }
}


