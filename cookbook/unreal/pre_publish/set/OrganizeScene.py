from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.unreal_engine.cli.organize_scene import organize_scene
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.unreal import alchemy as alc


class OrganizeScene(PreflightCheck):

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
        organize_scene()
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
