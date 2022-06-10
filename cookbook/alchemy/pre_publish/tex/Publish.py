from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.core.msd_tools import edit_publish_msd
import time


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
        user_object = self.shared_data['path_object']
        po = user_object.publish()
        time.sleep(5)  # TODO - this would be better to force this to wait until it's done.
        edit_publish_msd(user_object.user, po)
        self.pass_check('Check Passed')
        self.final_check()
