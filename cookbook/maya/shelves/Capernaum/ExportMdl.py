from cgl.plugins.maya.tasks.mdl import export_mdl
from cgl.plugins.maya.alchemy import scene_object
from cgl.core.utils.general import load_json, save_json


def run():
    path_object = scene_object()
    asset_name = path_object.asset
    msd_obj = path_object.copy(context='render', ext='msd')
    msd_path = msd_obj.path_root
    export_mdl(mesh=asset_name, ext='fbx')
    msd_json_obj = load_json(msd_path)
    msd_json_obj['updated'] = True
    save_json(msd_path, msd_json_obj)
    print("Exporting Selected")

