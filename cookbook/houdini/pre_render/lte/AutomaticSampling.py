from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.houdini import alchemy as alc


class AutomaticSampling(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Turn off automatic sampling in the scene to avoid long render times.
        """
        print('PreflightTemplate')
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
