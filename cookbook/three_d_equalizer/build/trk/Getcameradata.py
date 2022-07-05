#
# 3DE4.script.name: getcameradata
#
# 3DE4.script.version:
#
#


from cgl.plugins.three_d_equalizer.tasks.trk import set_camera_settings
from cgl.plugins.preflight.preflight_check import PreflightCheck
import shotgun_api3 as shotgrid



class Getcameradata(PreflightCheck):

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
        try:
            result_ = set_camera_settings()
        except RuntimeError:
            self.fail_check("Runtime Error: {}".format(RuntimeError.args))
            return

        if result_:
            self.pass_check('Check Passed')
        else:
            self.fail_check("Check Failed")
