import cgl.plugins.maya.alchemy as alc
import os
from cgl.ui.widgets.dialog import InputDialog


def replace_last(string, find, replace):
    reversed_ = string[::-1]
    replaced = reversed_.replace(find[::-1], replace[::-1], 1)
    return replaced[::-1]


def next_letter(letter):
    return chr((ord(letter.upper()) + 1 - 65) % 26 + 65)


def get_next_asset_name(path_object=None):
    if not path_object:
        path_object = alc.scene_object()
    asset = path_object.asset
    letter = asset[-1]
    new_letter = next_letter(letter)
    next_name = replace_last(asset, letter, new_letter)
    return next_name


def create_variant(variant=None):
    if not variant:
        so = alc.scene_object()
        next_name = get_next_asset_name(so)
    else:
        next_name = variant
    var_path = alc.scene_object().copy(shot=next_name, latest=True, set_proper_filename=True).path_root
    var_dir = os.path.dirname(var_path)
    if not os.path.exists(var_dir):
        os.makedirs(var_dir)
        os.makedirs(var_dir.replace('source', 'render'))
    alc.save_file_as(var_path)


def run():
    dialog = InputDialog(title='Create Variant', message='Create a Variant', line_edit=True)
    dialog.line_edit.setText(get_next_asset_name())
    dialog.exec_()
    if dialog.button == 'Ok':
        create_variant(dialog.line_edit.text())
        dialog.accept()
    else:
        dialog.accept()