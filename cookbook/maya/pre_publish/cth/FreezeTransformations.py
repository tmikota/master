from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.maya.tasks import mdl


class FreezeTransformations(PreflightCheck):

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
        mdl.freeze_transforms(name='mdl')
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
