# from cgl.plugins.unreal import alchemy as alc
import os
from cgl.core.path import PathObject
from cgl.core.utils.general import current_user, save_json
from cgl.plugins.unreal_engine.utils import get_source_path
import unreal


def run():
    selected_asset = unreal.EditorUtilityLibrary.get_selected_asset_data()
    asset_list = []
    tools = unreal.AssetToolsHelpers().get_asset_tools()
    workspace_path = unreal.SystemLibrary.convert_to_absolute_path(unreal.Paths.project_dir())
    project_name = unreal.Paths.get_base_filename(unreal.Paths.get_project_file_path())
    path_obj_source_path = get_source_path(workspace_path, project_name)
    path_object = PathObject(path_obj_source_path)

    for asset_ in selected_asset:
        category = 'prop'
        asset_class = asset_.get_class().get_name()
        if asset_class == "StaticMesh":
            asset_name = str(asset_.asset_name)
            asset_object = path_object.copy(seq=category, shot=asset_name, task='mdl', scope='assets',
                                            context='render', latest=True,
                                            user=current_user())
            source_path_object = asset_object.copy(context='source', latest=True)

            render_export_root = os.path.dirname(asset_object.next_major_version().path_root)
            if not os.path.exists(render_export_root):
                os.makedirs(render_export_root)
            msd_path_root = os.path.dirname(source_path_object.next_major_version().path_root)
            if not os.path.exists(msd_path_root):
                os.makedirs(msd_path_root)

            render_export_path_fbx = os.path.join(render_export_root, asset_name) + ".fbx"
            render_export_path_obj = os.path.join(render_export_root, asset_name) + ".obj"

            export_task_fbx = unreal.AssetExportTask()
            export_task_fbx.set_editor_property("object", asset_.get_asset())
            export_task_fbx.set_editor_property("filename", render_export_path_fbx)
            export_task_fbx.set_editor_property("automated", True)
            export_task_fbx.set_editor_property("prompt", False)
            export_task_fbx.set_editor_property("exporter", unreal.StaticMeshExporterFBX())
            export_options = unreal.FbxExportOption()
            export_task_fbx.set_editor_property("options", export_options)
            unreal.Exporter.run_asset_export_task(export_task_fbx)

            export_task_obj = unreal.AssetExportTask()
            export_task_obj.set_editor_property("object", asset_.get_asset())
            export_task_obj.set_editor_property("automated", True)
            export_task_obj.set_editor_property("prompt", False)
            export_task_obj.set_editor_property("exporter", unreal.StaticMeshExporterOBJ())
            export_task_obj.set_editor_property("filename", render_export_path_obj)
            unreal.Exporter.run_asset_export_task(export_task_obj)

            new_path = str(asset_.package_name).replace("/Game/", "") + ".uasset"
            full_asset_path = content_path + new_path
            asset_msd_dict = {
                "workspace_path": full_asset_path
            }
            asset_msd_path = os.path.join(msd_path_root, asset_name) + ".msd"
            save_json(filepath=asset_msd_path, data=asset_msd_dict)
