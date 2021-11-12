import bpy
import os
from pathlib import Path
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.object.select_all(action='DESELECT')
file3 = open("objfile.txt","r+")
objpath=file3.read()
objpath=objpath.lstrip("file:")
file3.close()
file4 = open("finalloc.txt","r+")
finloc=file4.read()
finloc=finloc.strip("file:")
file4.close()
bpy.ops.import_scene.obj(filepath=objpath)
with open("images.txt","r+") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

for i in lines:
    i=i.strip(" file:")
    i=i.strip("file:")
    if i !='':
        print(i)
        mat = bpy.data.materials.new(name="New_Mat")
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes["Principled BSDF"]
        texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
        texImage.image = bpy.data.images.load(i)
        mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])
        bpy.ops.object.select_all(action='SELECT')
        all = [item.name for item in bpy.data.objects]
        filename, file_extension = texImage.image.name.split(".")
        for name in all:
            if bpy.data.objects[name].type=='MESH':
                bpy.context.view_layer.objects.active = bpy.data.objects[name]
                ob = bpy.context.view_layer.objects.active
                for i in range(len(ob.material_slots)):
                    bpy.ops.object.material_slot_remove({'object': ob})
                ob.active_material_index = 0
                ob.data.materials.append(mat)
        Path(f"{finloc}/{filename}").mkdir(parents=True,exist_ok=True)
        bpy.ops.export_scene.obj(filepath=f"{finloc}/{filename}/{filename}.obj",use_materials=True,path_mode='ABSOLUTE',check_existing=False)
    else:
        print("Empty Filepath")

