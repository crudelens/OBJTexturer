# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from typing import List
import subprocess
import getpass
list2=[".bmp",".tif", ".tiff",".hdr",".exr",".dpx",".cin",".tga",".j2c",".jp2",".jpg",".jpeg",".png",".bw",".sgi",".rgb",".bmp"]
class MainWindow:
    
    def blendfinder(self,loc):
        file1 = open("blendloc.txt","w+")
        location=Path(loc)
        file1.write(str(location))
        file1.close()
        compareloc=os.path.basename(location)
        print(compareloc)
        if compareloc.lower()== "blender.exe" or compareloc.lower() == "blender.app" :
            print("Preset Blender Location:" + loc)
            objloc=input("Input OBJ File: ")
            objloc=objloc.strip()
            objloc=objloc.strip("'")
            self.objfinder(objloc)
        else:
            print("INVALID BLENDER DIRECTORY")
            loc2=input("Enter Blender Directory:")
            location2=loc2.strip()
            location2=location2.strip("'")
            self.blendfinder(location2)

    def objfinder(self,loc):
        location=Path(loc)
        filename, file_extension = os.path.splitext(location)
        if file_extension == ".obj" or file_extension == ".OBJ" :
            print(filename + " accepted")
            file4 = open("objfile.txt","w")
            file4.write(loc)
            file4.close()
            imgloc= input("Input Image Directory: ")
            imgloc=imgloc.strip()
            imgloc=imgloc.strip("'")
            if os.path.isdir(imgloc):
                imglist=os.listdir(imgloc)
                self.imgfinder(imgloc,imglist)
            else:
                print("Invalid Image Directory. Make sure input is a folder.")
                self.objfinder(loc)

        else:
            print("INVALID OBJECT DIRECTORY, make sure the file extension is .obj")
            loc2=input("Input OBJ File: ")
            location2=loc2.strip()
            location2=location2.strip("'")
            self.objfinder(location2)

    def imgfinder(self,imgloc,imglist):
        listimg=imglist
        for i in listimg:
            try:
                i=os.path.join(imgloc,i)
                filename, file_extension = os.path.splitext(i)
                if file_extension in list2:
                    print(f"Image {i} Added.")
                    file2 = open("images.txt","a+")
                    file2.write(f"{str(i)} \n")
                    file2.close() 
                else:
                    listimg.remove(i)       
            except:
                print(f"Image {i} Unsupported!!")
        if os.stat("images.txt").st_size != 0:
            finalloc=input("Output Directory: ")
            finalloc=finalloc.strip()
            finalloc=finalloc.strip("'")
            if os.path.isdir(finalloc):
                self.locwriter(finalloc)
            else:
                print("Output Directory not found. Please try again.")
                self.imgfinder(imgloc,imglist)

        else:
            print("No valid images found in directory")


        
    

    def render(self,blenddir):
        self.MYDIR=f"{Path(__file__).parent.absolute()}"
        print(self.MYDIR)
        blend=Path(blenddir.lstrip("file:"))
        subprocess.run([f"{blend}/Contents/MacOS/Blender","-b","-P", f"{self.MYDIR}/blendscript2.py"])
    

    def render2(self,blenddir):
        self.MYDIR=f"{Path(__file__).parent.absolute()}"
        print(self.MYDIR)
        blend=Path(blenddir.lstrip("file:"))
        p = subprocess.Popen([f"{blend}/Contents/MacOS/Blender","-b","-P", f"{self.MYDIR}/blendscript.py"], stderr=subprocess.PIPE, stdout=subprocess.PIPE,  stdin=subprocess.PIPE)
        output = p.stdout.read()
        print(output)

    def locwriter(self,loc):
        file4 = open("finalloc.txt","w+")
        file4.write(loc)
        file4.close()
        rendinp=input("Do you want to export OBJ (type: obj) or turntable (type: tt)? ")
        file = open("blendloc.txt", "r+")
        blendloc = file.read()
        print(rendinp)
        if rendinp.lower()=="obj":
            self.render2(blendloc)
        elif rendinp.lower()=="tt":
            self.render(blendloc)
        else:
            print("Unrecognised input. Please try again")
            self.locwriter(loc)
            
        


    def delimg(self):
        file2 = open("images.txt","w+")
        file2.truncate(0)
        

if __name__ == "__main__":
    file1 = open("blendloc.txt","r+")
    loc=file1.read()
    file1.close()
    file2 = open("images.txt","w+")
    file2.truncate(0)
    file2.close()
    file3 = open("objfile.txt","w+")
    file3.truncate(0)
    file3.close()
    location=loc.strip()
    location=location.strip("'")
    print(location)
    m=MainWindow()
    m.blendfinder(location)
    


