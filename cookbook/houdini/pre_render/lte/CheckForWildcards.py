from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.houdini import alchemy as alc


class CheckForWildcards(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Flag anything with "*" in magic list to allow the artist to make it more verbose.
        """
        print('PreflightTemplate')
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
