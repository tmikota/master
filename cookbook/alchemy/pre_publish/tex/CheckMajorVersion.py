from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.alchemy import magic_browser


class CheckMajorVersion(PreflightCheck):

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
        po = self.shared_data['path_object']
        if po.version.endswith('.000'):
            self.pass_check('Major Version Detected, check passes')
        else:
            self.fail_check('Minor version {} detected, version Up Selected, \n'
                            'then Choose "Major" as a version type'.format(po.version))
