import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button{
    id: btnLeftMenu
    text: qsTr("Home")
    display: AbstractButton.IconOnly
    implicitWidth: 250
    implicitHeight: 60
    //CUSTOM_PROPERTIES
    property url btnIconSource: "../../images/svg_images/home_icon.svg"
    property color colorDefault: "#D96704"
    property color colorMouseOver: "#F29F05"
    property color colorPressed: "#F2B705"
    property int iconWidth: 18
    property int iconHeight: 18
    property color borderColorDefault: "#c00"
    property color borderColorMouseOver: "#55aaff"
    property bool isActiveMenu: false
    visible: true
    QtObject{
        id: internal
        property var dynamicColor: if(btnLeftMenu.down){
                                       btnLeftMenu.down ? colorPressed : colorDefault
                                   } else {
                                       btnLeftMenu.hovered ? colorMouseOver : colorDefault
                                   }

        property var borderColor: if(btnLeftMenu.down){
                                      btnLeftMenu.down ? colorPressed : borderColorDefault
                                  }
                                      else{
                                   btnLeftMenu ? borderColorMouseOver: borderColorDefault
                                  }
    }

    background: Rectangle{
        anchors.fill: parent
        id:bgBtn
        color: internal.dynamicColor
        Rectangle{
            anchors{
                top: parent.top
                left: parent.left
                bottom: parent.bottom
            }
            color: internal.borderColor
            width: 5
            visible: isActiveMenu
        }
        Rectangle{
            anchors{
                top: parent.top
                right: parent.right
                bottom: parent.bottom
            }
            color: internal.borderColor
            width: 3
            visible: isActiveMenu
        }

        Image{
            id:iconBtn
            source: btnIconSource
            anchors.leftMargin: 26
            sourceSize.width: iconWidth
            sourceSize.height: iconHeight
            height: iconHeight
            width: iconWidth
            fillMode: Image.PreserveAspectFit
            visible: false
            antialiasing: true
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left

        }

        ColorOverlay{
            anchors.fill: iconBtn
            source: iconBtn
            color: "#ffffff"
            antialiasing: true
            height: iconHeight
            width: iconWidth
        }

        Text{
            color: "#ffffff"
            text: btnLeftMenu.text
            font: btnLeftMenu.font
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.leftMargin: 75
        }
      }
}



/*##^##
Designer {
    D{i:0;height:40;width:250}
}
##^##*/
