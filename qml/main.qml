import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "controls"
import QtQuick.Dialogs 1.0


Window {
    width: 1000
    height: 1000
    visible: true
    title: qsTr("OBJTexturer")
    
    QtObject{
        id: internal
        property url imagedir
        function makeobjvisible(){
            openobj.visible=true
            openobjlabel.visible=true
            chooseobjdir.visible=true
            objSeperator.visible=true
        }
        function makeimgvisible(){
            openimg.visible=true
            openimglabel.visible=true
            chooseimgdir.visible=true
            imgSeperator.visible=true
        }
        function hideall(){
            openobj.visible=false
            openobjlabel.visible=false
            chooseobjdir.visible=false
            objSeperator.visible=false
            openimg.visible=false
            openimglabel.visible=false
            chooseimgdir.visible=false
            imgSeperator.visible=false
            scrollView.visible=false
        }
    }

    FontLoader { id: webFont; source: "../Lovelo/Lovelo_Line_Light.otf" }
    Rectangle {
        id: bg
        color: "#0e0026"
        anchors.fill: parent

        TextField {
            id: blenderdir
            x: 532
            width: 282
            height: 40
            color: "#0e0026"
            anchors.right: chooseblenderdir.left
            anchors.top: parent.top
            font.weight: Font.Light
            anchors.rightMargin: 36
            anchors.topMargin: 50
            placeholderTextColor: "#5e00ff"
            font.family: "Courier"
            placeholderText: qsTr("Locate blender.exe/Blender.app")
            background: Rectangle { color: "#ff9d00" }
        }

        Label {
            id: openblenderlabel
            color: "#ffffff"
            text: qsTr("Choose Blender Directory")
            anchors.left: parent.left
            anchors.top: parent.top
            horizontalAlignment: Text.AlignLeft
            font.pointSize: 24
            font.styleName: "Line Light"
            font.family: "Lovelo"
            anchors.leftMargin: 50
            anchors.topMargin: 50
        }
        Label {
            id: blenderlabel
            color: "#ffffff"
            text: qsTr("Blender Directory")
            anchors.right: parent.right
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 10
            font.styleName: "Black"
            font.family: "Lovelo"
            anchors.rightMargin: 56
            anchors.topMargin: 100
        }

        TopBarButton {
            id: chooseblenderdir
            x: 904
            width: 40
            height: 40
            visible: true
            text: qsTr("Button")
            anchors.right: parent.right
            anchors.top: parent.top
            flat: false
            display: AbstractButton.IconOnly
            anchors.rightMargin: 56
            anchors.topMargin: 50
            icon.name: "open"
            btnIconSource: "../Images/svg_images/open_icon.svg"
            onPressed: {
                blendfileDialog.open()
            }
        }

        FileDialog {
            id: blendfileDialog
            title: "Please choose blender.exe or Blender.app"
            folder: shortcuts.home
            onAccepted: {
                console.log("You chose: " + blendfileDialog.fileUrls)
                backend.blendfinder(blendfileDialog.fileUrls)
            }
            onRejected: {
                console.log("Canceled")
            }
        }

        ToolSeparator {
            id: blenSeperator
            x: 541
            anchors.top: parent.top
            anchors.topMargin: 50
        }

        ToolSeparator {
            id: toolSeparator1
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: openblenderlabel.bottom
            anchors.topMargin: 50
            anchors.leftMargin: 50
            anchors.rightMargin: 50
            orientation: Qt.Horizontal
        }

        TextField {
            id: openobj
            x: 590
            width: 282
            height: 40
            color: "#0e0026"
            text: ""
            anchors.right: chooseobjdir.left
            anchors.top: toolSeparator1.bottom
            placeholderTextColor: "#5e00ff"
            font.family: "Courier"
            background: Rectangle {
                color: "#ff9d00"
            }
            anchors.rightMargin: 36
            font.weight: Font.Light
            anchors.topMargin: 50
            placeholderText: qsTr("Import 3D Object (.obj)")
            visible: false
        }

        Label {
            id: openobjlabel
            width: 273
            height: 40
            color: "#ffffff"
            text: qsTr("IMPORT OBJ FILE")
            anchors.left: parent.left
            anchors.top: toolSeparator1.bottom
            horizontalAlignment: Text.AlignLeft
            font.family: "Lovelo"
            anchors.leftMargin: 50
            font.styleName: "Line Light"
            anchors.topMargin: 50
            font.pointSize: 24
            visible : false
        }

        TopBarButton {
            id: chooseobjdir
            x: 908
            width: 40
            height: 40
            text: qsTr("Button")
            anchors.right: parent.right
            anchors.top: toolSeparator1.bottom
            display: AbstractButton.IconOnly
            anchors.rightMargin: 50
            icon.name: "open"
            flat: false
            anchors.topMargin: 50
            btnIconSource: "../Images/svg_images/open_icon.svg"
            visible : false
            onPressed: {
                objfileDialog.open()
            }
        }

        FileDialog {
            id: objfileDialog
            title: "Please choose your Object file"
            folder: shortcuts.home
            onAccepted: {
                console.log("You chose: " + objfileDialog.fileUrls)
                backend.objfinder(objfileDialog.fileUrls)
            }
            onRejected: {
                console.log("Canceled")
            }
        }

        ToolSeparator {
            id: objSeperator
            x: 541
            anchors.top: toolSeparator1.bottom
            anchors.topMargin: 50
            visible : false
        }

        TextField {
            id: openimg
            x: 590
            width: 282
            height: 40
            color: "#0e0026"
            text: ""
            anchors.right: chooseimgdir.left
            anchors.top: toolSeparator1.bottom
            hoverEnabled: true
            placeholderTextColor: "#5e00ff"
            font.weight: Font.Light
            anchors.topMargin: 168
            font.family: "Courier"
            anchors.rightMargin: 34
            background: Rectangle {
                color: "#ff9d00"
            }
            placeholderText: qsTr("Import Texture Images")
            visible : false
        }

        Label {
            id: openimglabel
            width: 461
            height: 40
            color: "#ffffff"
            text: qsTr("Import image files/folder")
            anchors.left: parent.left
            anchors.top: toolSeparator1.bottom
            horizontalAlignment: Text.AlignLeft
            font.pointSize: 24
            anchors.topMargin: 168
            font.family: "Lovelo"
            anchors.leftMargin: 50
            font.styleName: "Line Light"
            visible : false
        }

        TopBarButton {
            id: chooseimgdir
            x: 908
            width: 40
            height: 40
            text: qsTr("Button")
            anchors.right: parent.right
            anchors.top: toolSeparator1.bottom
            anchors.topMargin: 168
            anchors.rightMargin: 52
            flat: false
            icon.name: "open"
            btnIconSource: "../Images/svg_images/open_icon.svg"
            display: AbstractButton.IconOnly
            visible : false
            onPressed: {
                imgfileDialog.open()
            }
        }

        FileDialog {
            id: imgfileDialog
            title: "Please choose Image Files"
            selectMultiple: true
            folder: shortcuts.home
            onAccepted: {
                console.log(imgfileDialog.fileUrls)
                backend.imgfinder(imgfileDialog.fileUrls)
            }
            onRejected: {
                console.log("Canceled")
            }
        }

        ToolSeparator {
            id: imgSeperator
            x: 541
            y: 559
            anchors.top: toolSeparator1.bottom
            anchors.topMargin: 171
            visible : false
        }

        ScrollView {
            id: scrollView
            y: 449
            height: 406
            anchors.left: parent.left
            anchors.right: parent.right
            clip: true
            enabled: true
            anchors.rightMargin: 50
            anchors.leftMargin: 50
            visible : true

            Grid {
                id: grid
                anchors.fill: parent
                verticalItemAlignment: Grid.AlignVCenter
                horizontalItemAlignment: Grid.AlignHCenter
                clip: false
            }
        }
       CameraBtn{
           id:renderimages
           y: 880
           width: 311
           height: 40
           text: qsTr("Render Images")
           anchors.left: parent.left
           anchors.bottom: parent.bottom
           colorPressed: "#95286e"
           anchors.leftMargin: 125
           textdef: qsTr("Render Images")
           checkable: false
           anchors.bottomMargin: 80
           visible: false
           onPressed: {
               finfileDialog.open()
            }

       }
       FileDialog {
            id: finfileDialog
            title: "Please choose Image Files"
            selectFolder: true
            folder: shortcuts.home
            onAccepted: {
                backend.locwriter(finfileDialog.fileUrls)
                backend.render(blenderdir.text)
                //backend.render(openobj.text,blenderdir.text)
            }
            onRejected: {
                console.log("Canceled")
            }
       }


        CameraBtn {
            id: deleteimages
            visible: false
            text: qsTr("Render Images")
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            colorPressed: "#f205bc"
            colorMouseOver: "#a505f2"
            colorDefault: "#89326c"
            textdef: qsTr("Delete All Images")
            anchors.bottomMargin: 20
            checkable: false
            onPressed: {
                for(var i = grid.children.length; i > 0 ; i--) {
                    console.log("destroying: " + i)
                    grid.children[i-1].destroy()
                }
                renderimages.visible=false;
                renderobj.visible=false;
                deleteimages.visible=false;
                backend.delimg()
            }
        }

        CameraBtn {
            id: renderobj
            y: 880
            width: 311
            height: 40
            visible: false
            text: qsTr("Save OBJs")
            anchors.left: parent.left
            anchors.bottom: parent.bottom
            colorPressed: "#95286e"
            colorMouseOver: "#e95f00"
            colorDefault: "#ff9800"
            checkable: false
            textdef: qsTr("Save OBJs")
            anchors.bottomMargin: 80
            anchors.leftMargin: 572
            onPressed: {
               backend.render2(blenderdir.text)
            }
        }
    }
    Connections{
        target: backend

        function onSetName(name){
            blenderlabel.text = name
            blenderdir.text = name
            if (name !== "INVALID BLENDER DIRECTORY"){
                internal.makeobjvisible()
            } else {
                internal.hideall()
            }
        }
        function onSetObj(objname){
            openobj.text = objname
            if (objname !== "INVALID OBJECT DIRECTORY"){
                internal.makeimgvisible()
            }

        }
        function onSetImg(imgname){
            var n = imgname.split("/");
            var img=n[n.length - 1];
            var finim= img.split(".");
            var fin=finim[finim.length-2];
            var fin2=fin.toLowerCase();
            var fin3=fin2.replace(" ", "_");
            var finfr='i_'+fin3
            console.log(finfr)
            var newObject = Qt.createQmlObject('import QtQuick 2.0; Image {id: ' + finfr + '; source: "' + imgname + '"; width: 192; height: 108; fillMode: Image.PreserveAspectFit }',
                                               grid,
                                               finfr);
            if (newObject === null) {
                // Error Handling
                console.log("Error creating object");
            } else{
                renderimages.visible=true;
                renderobj.visible=true;
                deleteimages.visible=true;
            }
        }
    }
}



/*##^##
Designer {
    D{i:0;formeditorZoom:0.66}D{i:1}D{i:2}D{i:4}D{i:6}D{i:7}D{i:8}D{i:9}D{i:10}D{i:11}
D{i:12}D{i:14}D{i:15}D{i:16}D{i:17}D{i:18}D{i:20}D{i:21}D{i:22}D{i:23}D{i:25}D{i:24}
D{i:26}D{i:27}D{i:28}D{i:29}D{i:3}D{i:30}
}
##^##*/
