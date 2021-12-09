from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya import alchemy as alc


class NextMajorVersion(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Version Up to Next Major Version
        """
        alc.version_up(vtype='major')
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
