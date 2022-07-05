from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya import alchemy as alc


class VersionUp(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        versions up one major version, copies everythging in the render directory as well as the source directory.
        :return:
        """
        alc.version_up(vtype='major', copy_render=True)
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
