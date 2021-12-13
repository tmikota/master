from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
import pymel.core as pm


class RigTopNode(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Checks for a top node called "rig"
        """
        if pm.objExists('rig'):
            self.pass_check('Found "rig", check Passed')
        else:
            self.fail_check('No group named "rig", check Failed')

