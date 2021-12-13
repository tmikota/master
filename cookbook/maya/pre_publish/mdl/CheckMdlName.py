from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya.tasks import mdl
import pymel.core as pm


class CheckMdlName(PreflightCheck):

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
        if pm.objExists('mdl'):
            self.pass_check('Check Passed')
        else:
            self.fail_check('"mdl" group does not exist, check failed')
        # self.fail_check('Check Failed')
