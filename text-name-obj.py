bl_info = {
    "name": "Object Name Text",
    "author": "Fedir Gontsa",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Text > Object Name",
    "description": "This add-on creates the name of the selected object above it as a signature on the map at a height of 3 units along the Z axis with a 90-degree rotation relative to the X axis",
    "category": "Text"
}

import bpy
from mathutils import Vector
from math import radians

def create_text_from_box():
    # get the selected object
    obj = bpy.context.active_object
    
    # check if the selected object is a mesh
    if obj.type == 'MESH':
        # create a new text object
        text_obj = bpy.data.objects.new("Text", bpy.data.curves.new(type="FONT", name="Font"))
        
        # set the text to the box's name
        text_obj.data.body = obj.name
        
        # set the text's location to be on top of the box
        offset = Vector((0, 0, 3))  # adjust the offset as needed
        
        text_obj.location = obj.location + offset
        text_obj.rotation_euler.x += radians(90)
        
        
        # add the text object to the scene
        bpy.context.scene.collection.objects.link(text_obj)

# call the function
create_text_from_box()