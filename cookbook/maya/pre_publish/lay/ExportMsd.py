from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
import cgl.plugins.maya.tasks.lay as lay


class ExportMsd(PreflightCheck):

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
        lay.Task().export_msd(self.shared_data['publish_object'])
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
