import pymel.core as pm
from cgl.plugins.maya.alchemy import scene_object, import_file

def run():
    path_object = scene_object()
    fbx_path_object = path_object.copy(context='render', ext='fbx')
    import_file(fbx_path_object.path_root, namespace='assets')