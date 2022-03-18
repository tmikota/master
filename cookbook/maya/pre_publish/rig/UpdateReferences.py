from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya import utils as utils


class UpdateReferences(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        update the references in the scene
        """
        utils.update_all_references()
        self.pass_check('Check Passed')
        # if utils.update_all_references():
        #     self.pass_check('Check Passed')
        # else:
        #     self.fail_check('Check Failed')
