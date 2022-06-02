from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya.tasks import mdl


class CheckGeoResolution(PreflightCheck):

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
        if mdl.get_mdl_resolutions(check=True):
            self.pass_check('High & Low Geometry Resolutions Found')
        else:
            self.fail_check('High & Low Geometry Resolutions Not Found, Please Create at least one of them')
