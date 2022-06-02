from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.houdini import alchemy as alc


class AddMetadataToExr(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        We're looking to add metadata to the exr of render time per bucket, or some kind of heat map for buckets...
        """
        print('PreflightTemplate')
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
