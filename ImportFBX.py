## Importscript for .FBX .fbx files
## no backslash support \
## no double slash support //

# load Blender Python API's
import bpy, os

# Delet all Stuff (cube?) 1=yes 0=no 
delet_all = '1' 

# Customize the path to your FBX files folder
fbx_folder = "C:/Users/warsh/Documents/Unreal Projects/Blender/Diriyah/Mesh/"

# remove the Cube/Cam/Light
if delet_all == '1':
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

# Get the Cube Collection and delet it 
    cube_collection = bpy.context.collection
    bpy.data.collections.remove(cube_collection)

# List of all FBX files in the folder!
fbx_files = [f for f in os.listdir(fbx_folder) if f.endswith('.fbx') or f.endswith('.FBX')]

# Loop through the list of FBX files
for fbx_file in fbx_files:
    file_path = os.path.join(fbx_folder, fbx_file)

# Import the FBX files
    bpy.ops.import_scene.fbx(filepath=file_path)

# List of all Subfolders in the folder!
fbx_subfolders = [f for f in os.listdir(fbx_folder) if os.path.isdir(os.path.join(fbx_folder, f))]

# Loop through the list of Subfolders
for fbx_subfolder in fbx_subfolders:
    sub_path = os.path.join(fbx_folder, fbx_subfolder)

# New collection with the name of the subfolder
    myCol = bpy.data.collections.new(fbx_subfolder)
    bpy.context.scene.collection.children.link(myCol)

# List of all FBX files in the subfolder
    fbx_subfiles = [f for f in os.listdir(sub_path) if f.endswith('.fbx') or f.endswith('.FBX')]
    
# Loop through the list of FBX files in the subfolder
    for fbx_subfile in fbx_subfiles:
        file_subpath = os.path.join(sub_path, fbx_subfile)
        
# Import the FBX files
        bpy.ops.import_scene.fbx(filepath=file_subpath)
        
# get the aktiv collection of the FBX file
        aktiv_collection= bpy.context.collection
		
# Link the FBX files to the Subfolder Collection
        myCol.objects.link(bpy.context.selected_objects[0])

# Unlink the FBX files from the aktiv Collection
        aktiv_collection.objects.unlink(bpy.context.selected_objects[0])