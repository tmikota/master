from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.alchemy import magic_browser


class VersionUpMajor(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Version Up to a Major Version before publishing.
        """
        print('PreflightTemplate')
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
