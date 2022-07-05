from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.SOFTWARE import alchemy as alc
from cgl.plugins.three_d_equalizer.tasks.trk import export_maya_file
import sys


class Exportmaya(PreflightCheck):

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
        print('PreflightTemplate')
        try:
            export_maya_file()
        except RuntimeError:
            self.fail_check("Runtime Error: {}".format(RuntimeError.args))
            return
        self.pass_check('Check Passed')
