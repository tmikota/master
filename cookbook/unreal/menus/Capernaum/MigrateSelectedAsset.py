from PySide2 import QtWidgets, QtGui, QtUiTools, QtCore
from cgl.ui.widgets.dialog import InputDialog
from cgl.plugins.unreal_engine.utils import get_source_path,  get_unreal_projects, migrate_selected_assets
from cgl.core.path import PathObject
import sys
import unreal


def run():
    workspace_path = unreal.SystemLibrary.convert_to_absolute_path(unreal.Paths.project_dir())
    project_name = unreal.Paths.get_base_filename(unreal.Paths.get_project_file_path())
    path_obj_source_path = get_source_path(workspace_path, project_name)
    path_object = PathObject(path_obj_source_path)

    project_dict = get_unreal_projects(path_object)
    uproject_list = []

    for uproject_name in project_dict:
        uproject_list.append(uproject_name)
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)
    level_selector = InputDialog(title="Migration Tool", message="Select Destination Project", combo_box_items=uproject_list)
    level_selector.show()
    app.exec_()
    if level_selector.button == 'Ok':
        selected_asset = level_selector.combo_box.currentText()
        uproject_path = project_dict[selected_asset]['uproject_path'] + "\\"
        migrate_selected_assets(migrate_root=uproject_path)


if __name__ == '__main__':
    run()