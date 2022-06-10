from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.maya import alchemy as alc
from cgl.core.msd_tools import edit_publish_msd

class Publish(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Publishes the current major version, edits the published .msd file accordingly.
        Returns:

        """
        user_object = alc.scene_object()
        print(user_object.user)
        po = user_object.publish()
        print(po.path_root)
        edit_publish_msd(user_object.user, po)
        self.pass_check('Check Passed')
