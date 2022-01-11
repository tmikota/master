from cgl.plugins.unreal_engine.utils import migrate_selected_asset
from cgl.ui.widgets.dialog import InputDialog


def run():
    level_selector = InputDialog(title="Select Level", message="Select Project to Migrate to")
    level_selector.exec_()
    dest_uproject_path = r'C:\Users\VP01\Documents\Unreal Projects\MigrationTest\MigrationTest.uproject'
    migrate_selected_asset(destination_uproject_path=dest_uproject_path)


if __name__ == '__main__':
    run()