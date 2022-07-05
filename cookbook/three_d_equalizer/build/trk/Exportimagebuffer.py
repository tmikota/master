#
# 3DE4.script.name: exportimagebuffer
#
# 3DE4.script.version:
#
#

from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.core.utils.general import cgl_execute
from exportFastBufferCompression import compress
import tde4
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.SOFTWARE import magic_browser


class Exportimagebuffer(PreflightCheck):

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
            cams = tde4.getCameraList()
            compress(cams, ui=True)
        except RuntimeError as error_:
            self.fail_check("Runtime Error: {}".format(error_))
            return
        self.pass_check('Check Passed')

