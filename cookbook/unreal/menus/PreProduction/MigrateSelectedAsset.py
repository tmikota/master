from cgl.plugins.unreal_engine.utils import migrate_selected_asset

def run():
    dest_uproject_path = r'C:\Users\VP01\Documents\Unreal Projects\MigrationTest\MigrationTest.uproject'
    migrate_selected_asset(destination_uproject_path=dest_uproject_path)
