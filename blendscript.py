import bpy
import os
from pathlib import Path

from bpy.types import Image
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.object.select_all(action='DESELECT')
file3 = open("objfile.txt","r+")
objpath=file3.read()
objpath=objpath.lstrip("file:")
file3.close()
file = open("finalloc.txt","r+")
finloc=file.read()
file.close()
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
        target=os.path.join(finloc, "OBJExports", filename)
        try:
            os.makedirs(target, mode = 0o777, exist_ok = False)
        except:
            pass
        bpy.ops.export_scene.obj(filepath=f"{target}/{filename}.obj", check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=False, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
    else:
        print("Empty Filepath")

