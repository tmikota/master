# from cgl.plugins.unreal import alchemy as alc
from cgl.core.path import PathObject
from cgl.plugins.unreal_engine.utils import update_mesh, get_asset_task, get_source_path
import unreal


def run():
    workspace_path = unreal.SystemLibrary.convert_to_absolute_path(unreal.Paths.project_dir())
    project_name = unreal.Paths.get_base_filename(unreal.Paths.get_project_file_path())
    path_obj_source_path = get_source_path(workspace_path, project_name)
    path_object = PathObject(path_obj_source_path)

    selected_actor = unreal.EditorLevelLibrary.get_selected_level_actors()[0]
    asset_task = get_asset_task(selected_actor)
    if asset_task == "Mdl":
        update_mesh(asset=selected_actor, path_object=path_object)

