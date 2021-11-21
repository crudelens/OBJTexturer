# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from typing import List
from PySide2.QtCore import QObject,Slot,Signal
import subprocess
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
import getpass
list2=[".bmp",".tif", ".tiff",".hdr",".exr",".dpx",".cin",".tga",".j2c",".jp2",".jpg",".jpeg",".png",".bw",".sgi",".rgb",".bmp"]
class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)

    setName = Signal(str)
    
    @Slot(str)
    def blendfinder(self,loc):
        file1 = open("blendloc.txt","w+")
        location=Path(loc)
        file1.write(str(location))
        file1.close()
        compareloc=os.path.basename(location)
        if compareloc.lower()== "blender.exe" or compareloc.lower() == "blender.app" :
            self.setName.emit(loc)
        elif loc=="":
            pass
        else:
            self.setName.emit("INVALID BLENDER DIRECTORY")

    setObj = Signal(str)

    @Slot(str)
    def objfinder(self,loc):
        location=Path(loc)
        filename, file_extension = os.path.splitext(location)
        print(file_extension)
        if file_extension == ".obj" or file_extension == ".OBJ" :
            self.setObj.emit(loc)
            file3 = open("objfile.txt","w+")
            file3.write(loc)
            file3.close()
        else:
            self.setObj.emit("INVALID OBJECT DIRECTORY")

    setImg = Signal(str)
    @Slot(str)
    def imgfinder(self,imgloc):
        listimg=list(imgloc.split(","))
        for i in listimg:
            try:
                filename, file_extension = os.path.splitext(i)
                if file_extension in list2:
                    self.setImg.emit(i)
                    file2 = open("images.txt","a+")
                    file2.write(f"{str(i)} \n")
                    file2.close()
                else:
                    listimg.remove(i)
                    
            except:
                print("Image Unsupported")
    
    @Slot(str)
    def render(self,blenddir):
        self.MYDIR=f"{Path(__file__).parent.absolute()}"
        print(self.MYDIR)
        blend=Path(blenddir.lstrip("file:"))
        subprocess.run([f"{blend}/Contents/MacOS/Blender","-b","-P", f"{self.MYDIR}/blendscript2.py"])
    
    @Slot(str)
    def render2(self,blenddir):
        self.MYDIR=f"{Path(__file__).parent.absolute()}"
        print(self.MYDIR)
        blend=Path(blenddir.lstrip("file:"))
        p = subprocess.Popen([f"{blend}/Contents/MacOS/Blender","-b","-P", f"{self.MYDIR}/blendscript.py"], stderr=subprocess.PIPE, stdout=subprocess.PIPE,  stdin=subprocess.PIPE)
        output = p.stdout.read()
        print(output)

    @Slot(str)
    def locwriter(self,loc):
        file4 = open("finalloc.txt","w+")
        file4.write(loc)
        file4.close()

    @Slot()
    def delimg(self):
        file2 = open("images.txt","w+")
        file2.truncate(0)
        

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    main = MainWindow()
    engine.rootContext().setContextProperty("backend",main)
    engine.load(os.fspath(Path(__file__).resolve().parent / "qml/main.qml"))
    file1 = open("blendloc.txt","r+")
    blenddir=file1.read()
    file1.close()
    file2 = open("images.txt","w+")
    file2.truncate(0)
    file2.close()
    file3 = open("objfile.txt","w+")
    file3.truncate(0)
    file3.close()
    main.blendfinder(blenddir)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
