from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.houdini import alchemy as alc


class SetUpRenderStats(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        We want to be able to put bucket render times into the exr somehow (maybe as a post process, maybe as an AOV?)
        """
        print('PreflightTemplate')
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
