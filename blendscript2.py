import bpy
import os
from pathlib import Path
bpy.data.scenes[0].frame_end=120
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.object.select_all(action='DESELECT')
bpy.context.scene.render.film_transparent = True
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (1, 1, 1, 1)
file3 = open("objfile.txt","r+")
objpath=file3.read()
objpath=objpath.lstrip("file:")
file3.close()
file4 = open("finalloc.txt","r+")
finloc=file4.read()
finloc=finloc.strip("file:")
file4.close()
bpy.ops.import_scene.obj(filepath=objpath)
all = [item.name for item in bpy.data.objects]
for name in all:
    bpy.context.view_layer.objects.active= bpy.data.objects[name]
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.join()
bpy.ops.object.camera_add()
bpy.ops.object.constraint_add(type='TRACK_TO')
print(bpy.context.object.constraints["Track To"].target)
bpy.data.scenes["Scene"].camera=bpy.data.objects["Camera"]
bpy.context.scene.use_nodes = True
tree = bpy.context.scene.node_tree
for node in tree.nodes:
    tree.nodes.remove(node)

rl_node= tree.nodes.new(type="CompositorNodeRLayers")
mix_node= tree.nodes.new(type="CompositorNodeMixRGB")
mix_node.use_alpha=True
blur_node = tree.nodes.new(type='CompositorNodeBlur')
blur_node.size_x = 300
blur_node.size_y = 300
image_node = tree.nodes.new(type='CompositorNodeImage')
image_node.location = 0,0


# create output node
comp_node = tree.nodes.new('CompositorNodeComposite')   
comp_node.location = 400,0

# link nodes
links = tree.links
link = links.new(image_node.outputs[0], blur_node.inputs[0])
link2 = links.new(blur_node.outputs[0], mix_node.inputs[1])
link3 = links.new(rl_node.outputs[0], mix_node.inputs[2])
link4 = links.new(mix_node.outputs[0], comp_node.inputs[0])

with open("images.txt","r+") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
objname=""
dimx=None
hz=None
for i in lines:
    print(i)
    i=i.strip(" file:")
    i=i.strip("file:")
    if i !='':
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
                objname=name
                bpy.context.view_layer.objects.active = bpy.data.objects[name]
                ob = bpy.context.view_layer.objects.active
                for i in range(len(ob.material_slots)):
                    bpy.ops.object.material_slot_remove({'object': ob})
                ob.active_material_index = 0
                bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='MEDIAN')
                dimx=bpy.context.object.dimensions[0]
                hz=bpy.context.object.location[2]
                ob.data.materials.append(mat)
        lastframe=bpy.data.scenes[0].frame_end
        onefifth=int(lastframe/5)
        bpy.context.scene.frame_set(1)
        bpy.context.object.rotation_euler[2] = 1.0472
        bpy.context.object.rotation_euler[0] = 2
        ob.keyframe_insert("rotation_euler")
        bpy.context.scene.frame_set(onefifth*5)
        bpy.context.object.rotation_euler[2] = -5.235988
        ob.keyframe_insert("rotation_euler")
        bpy.data.objects["Camera"].location[1]=dimx*2
        bpy.data.objects["Camera"].location[2]=hz
        bpy.data.objects["Camera"].constraints["Track To"].target = bpy.data.objects[objname]
        image_node.image = bpy.data.images[texImage.image.name]
        bpy.data.scenes[0].render.filepath=f"{finloc}/{filename}"
        bpy.context.scene.frame_set(1)
        bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
        bpy.context.scene.render.ffmpeg.format = 'MPEG4'
        bpy.ops.render.render(animation=True)
    else:
        print("Empty Filepath")

