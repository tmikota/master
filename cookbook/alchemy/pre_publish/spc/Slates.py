from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.alchemy.tasks.spc as spc


class Slates(PreflightCheck):

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
        key_list = ["Shots Naming Pattern", "Shots Naming Regex", "Trailer Naming Pattern", "Trailer Naming Regex",
                    "Assets Naming Pattern", "Assets Naming Regex"]
        dialog = spc.SpecSheetEntry(title='Frame Numbers and Handles', key_list=key_list)
        dialog.exec_()
        self.pass_check('Check Passed')
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
