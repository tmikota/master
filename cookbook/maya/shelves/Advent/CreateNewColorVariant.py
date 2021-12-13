import cgl.plugins.maya.alchemy as alc
import os
from cgl.ui.widgets.dialog import InputDialog


def create_variant(variant):
    var_path = alc.scene_object().copy(variant=variant, latest=True).path_root
    var_dir = os.path.dirname(var_path)
    if not os.path.exists(var_dir):
        os.makedirs(var_dir)
        os.makedirs(var_dir.replace('source', 'render'))
    alc.save_file_as(var_path)


def run():
    dialog = InputDialog(title='Create Variant', message='Create a Variant (varB for example)', line_edit=True)
    dialog.exec_()
    if dialog.button == 'Ok':
        create_variant(dialog.line_edit.text())
        dialog.accept()
    else:
        dialog.accept()

