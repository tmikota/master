from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya import alchemy as alc


class SaveScene(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Save the Scene
        """
        alc.save_file()
        self.pass_check('Check Passed')
