from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya import alchemy as alc


class Publish(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Publish copies the current user source and render files into the "publish" user for further use down the
        pipeline.
        """
        alc.scene_object().publish()
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
