from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.houdini import alchemy as alc


class CheckForWildcards(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        This gives us the ability to flag any nodes with raw wildcards.   "*" in a node is typically expensive.   Use magic list to show everything to allow artist to fix it.
        """
        print('PreflightTemplate')
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
