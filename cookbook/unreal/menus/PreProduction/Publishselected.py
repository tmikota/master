# from cgl.plugins.unreal import alchemy as alc
import os
from cgl.core.path import PathObject
from cgl.core.config.config import ProjectConfig
from cgl.core.utils.general import current_user, save_json
from cgl.plugins.unreal_engine.utils import get_source_path, publish_static_mesh, publish_bndl, publish_layout, get_asset_task
import unreal


def run():
    workspace_path = unreal.SystemLibrary.convert_to_absolute_path(unreal.Paths.project_dir())
    project_name = unreal.Paths.get_base_filename(unreal.Paths.get_project_file_path())
    path_obj_source_path = get_source_path(workspace_path, project_name)
    company = '4th_wall'
    cfg = ProjectConfig(company=company)
    path_object = PathObject(path_obj_source_path, cfg)

    unique_mesh_list = []
    selected_actor = unreal.EditorLevelLibrary.get_selected_level_actors()[0]
    asset_task = get_asset_task(selected_actor)
    if asset_task == "Mdl":
        static_mesh = selected_actor.static_mesh_component.static_mesh
        publish_static_mesh(static_mesh, path_object)
    if asset_task == "Bndl":
        publish_bndl(selected_actor, path_object, unique_mesh_list)
    if asset_task == "Lay":
        publish_layout(selected_actor, path_object, unique_mesh_list)


if __name__ == '__main__':
    run()


