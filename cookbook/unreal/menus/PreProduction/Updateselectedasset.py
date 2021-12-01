# from cgl.plugins.unreal import alchemy as alc
from cgl.core.path import PathObject
from cgl.plugins.unreal_engine.utils import update_mesh, update_bndl, update_layout, get_asset_task, get_source_path
import unreal


def run():
    workspace_path = unreal.SystemLibrary.convert_to_absolute_path(unreal.Paths.project_dir())
    project_name = unreal.Paths.get_base_filename(unreal.Paths.get_project_file_path())
    path_obj_source_path = get_source_path(workspace_path, project_name)
    path_object = PathObject(path_obj_source_path)

    selected_actor = unreal.EditorLevelLibrary.get_selected_level_actors()[0]
    asset_task = get_asset_task(selected_actor)
    unique_mesh_list = []
    if asset_task == "Mdl":
        static_mesh = selected_actor.static_mesh_component.static_mesh
        update_mesh(static_mesh=static_mesh, path_object=path_object)
    if asset_task == "Bndl":
        update_bndl(asset=selected_actor, path_object=path_object, unique_mesh_list=unique_mesh_list)
    if asset_task == "Lay":
        update_layout(asset=selected_actor, path_object=path_object, unique_mesh_list=unique_mesh_list)


if __name__ == '__main__':
    run()