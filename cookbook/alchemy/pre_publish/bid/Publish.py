from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.alchemy import magic_browser


class Publish(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Publish the bid.
        :return:
        """
        # Publish this version
        po = self.shared_data['path_object'].publish()
        self.shared_data['publish_object'] = po
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
