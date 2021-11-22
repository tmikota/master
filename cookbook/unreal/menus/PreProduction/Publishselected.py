# from cgl.plugins.unreal import alchemy as alc
import os
from cgl.core.path import PathObject
from cgl.core.utils.general import current_user, save_json
from cgl.plugins.unreal_engine.utils import get_source_path, publish_static_mesh, publish_bndl, publish_layout, get_asset_task
import unreal


def run():
    # # selected_asset = unreal.EditorUtilityLibrary.get_selected_asset_data()
    # # asset_list = []
    #
    workspace_path = unreal.SystemLibrary.convert_to_absolute_path(unreal.Paths.project_dir())
    project_name = unreal.Paths.get_base_filename(unreal.Paths.get_project_file_path())
    path_obj_source_path = get_source_path(workspace_path, project_name)
    path_object = PathObject(path_obj_source_path)

    selected_actor = unreal.EditorLevelLibrary.get_selected_level_actors()[0]
    asset_task = get_asset_task(selected_actor)
    if asset_task == "Mdl":
        publish_static_mesh(selected_actor, path_object)
    print("Task: {}".format(asset_task))
    # root_comp = selected_actor.root_component
    # for comp in root_comp.get_children_components(True):
    #     # print(comp.get_class().get_name())
    #     if comp.get_class().get_name() == "ChildActorComponent":
    #         print(comp.get_name())


    # for asset_ in selected_asset:
    #     category = 'prop'
    #     asset_class = asset_.get_class().get_name()
    #     get_asset_task(asset_)
    #     # if asset_class == "StaticMesh":
    #     #     publish_static_mesh(asset_, path_object)


