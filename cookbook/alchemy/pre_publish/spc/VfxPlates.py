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
        try:
            path_object = self.shared_data['path_object']
            key_list = ['Color Space', 'Plate Naming Pattern', "Plate Naming Regex", "Main Plate", "Clean Plate"]
            dialog = spc.SpecSheetEntry(title='Frame Numbers and Handles', key_list=key_list, path_object=path_object)
            dialog.exec_()
        except RuntimeError:
            self.fail_check("Check Failed: {}".format(RuntimeError.args))

        self.pass_check('Check Passed')

