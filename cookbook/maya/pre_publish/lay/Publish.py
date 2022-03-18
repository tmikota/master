from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a lumbermill.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya import alchemy
import cgl.plugins.maya.tasks.lay as lay


class Publish(PreflightCheck):

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
        publish_object = alchemy.scene_object().publish()
        lay.Task().export_msd(publish_object)
        self.pass_check('Check Passed')

