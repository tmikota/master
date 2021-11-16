from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.unreal_engine.fg_tool import create_window
import unreal
import os
import shutil
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.unreal import alchemy as alc


class FgTool(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        script to be executed when the preflight is run.

        If the preflight is successful:
        self.pass_check('Message about a passed Check')

        if the preflight fails:
        self.fail_check('Message about a failed check')
        :return:
        """

        # project_dir_path = unreal.SystemLibrary.convert_to_absolute_path(unreal.Paths.project_dir())
        # widget_path = os.path.join(project_dir_path, "Content", "FG_Tool.uasset")
        # if os.path.exists(widget_path):
        #     print("YUHHH")
        # else:
        #     widget_source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content", "FGTool", "FG_Tool.uasset")
        #     shutil.copy(widget_source_path, widget_path)
        # create_window()
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
