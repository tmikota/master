from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.maya import alchemy as alc
import pymel.core as pm


class OrganizeAnimation(PreflightCheck):

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
        if not pm.objExists('ANIM'):
            # TODO - need to rebuild this function properly in anim task.
            #  for now we'll just make sure this exists.
            pm.select(cl=True)
            pm.group(name='ANIM')
            pm.select(cl=True)
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
