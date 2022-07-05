#
# 3DE4.script.name: importlidar
#
# 3DE4.script.version:
#
#

from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.three_d_equalizer.tasks.ldr import import_latest
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.SOFTWARE import magic_browser


class Importlidar(PreflightCheck):

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
        if import_latest():
            self.pass_check('Check Passed')
        else:
            self.fail_check('Check Failed')

