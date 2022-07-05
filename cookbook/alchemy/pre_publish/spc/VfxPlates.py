from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.alchemy.tasks.spc as spc


class VfxPlates(PreflightCheck):

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
        key_list = ['Color Space', 'Plate Naming Pattern', "Plate Naming Regex", "Main Plate", "Clean Plate"]
        dialog = spc.SpecSheetEntry(title='Frame Numbers and Handles', key_list=key_list)
        dialog.exec_()
        self.pass_check('Check Passed')

