from cgl.plugins.maya.alchemy import scene_object, reference_file
from cgl.core.path import PathObject
from cgl.ui.widgets.dialog import InputDialog
from cgl.plugins.maya.utils import select_reference
import glob
import pymel.core as pm


def run():
    so = scene_object().copy(task='rig',scope='assets', seq='*', shot='*', user='publish', version="*", filename="*", ext=None)
    asset_list = []
    asset_map = {}
    publishes = glob.glob(so.path_root)
    print(so.path_root)
    for file in publishes:
        path_object = PathObject(file)
        asset_map[path_object.asset] = path_object.path_root

    dialog_ = InputDialog(title="Import Rigs", message="Select Published Rig to Reference",
                          combo_box_items=asset_map.keys())
    dialog_.exec_()

    if dialog_.button == 'Ok':
        asset_name = dialog_.combo_box.currentText()
        file_path = asset_map[asset_name]
        ref = reference_file(file_path)
        select_reference(ref)
        pm.group(name='RIG')
