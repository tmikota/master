# from cgl.plugins.unreal import alchemy as alc
import unreal


def run():
    """
    This allows the user to select a camera, click the button and attach reference to the camera.
    :return:
    """
    #list = unreal.EditorUtilityLibrary.get_selected_assets()

    #print(unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(list[0]))


    selected = unreal.EditorLevelLibrary.get_selected_level_actors()
    #camera_path = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(selected[0])

    unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.EditorAssetLibrary.load_blueprint_class('/C:/Users/CMPAforgePC2/Documents/Unreal_Projects/ReplacingMats/Content/StarterContent/Shapes/Shape_Plane.uasset'), unreal.Vector(0.0, 0.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0))

if __name__ == '__main__':
    run()

