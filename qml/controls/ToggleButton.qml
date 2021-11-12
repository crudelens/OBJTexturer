import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button{
    id: btnToggle
    implicitWidth: 70
    implicitHeight: 60
    //CUSTOM_PROPERTIES
    property url btnIconSource: "../../images/svg_images/menu_icon.svg"
    property color colorDefault: "#D96704"
    property color colorMouseOver: "#F29F05"
    property color colorPressed: "#F2B705"
    QtObject{
        id: internal
        property var dynamicColor: if(btnToggle.down){
                                       btnToggle.down ? colorPressed : colorDefault
                                   } else {
                                       btnToggle.hovered ? colorMouseOver : colorDefault
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
            height: 25
            width: 25
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


