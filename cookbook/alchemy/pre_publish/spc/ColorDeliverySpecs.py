from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.alchemy.tasks.spc as spc


class ColorDeliverySpecs(PreflightCheck):

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
        key_list = ["CDL Sidecar (True/False)", "Delivery Color Space"]
        dialog = spc.SpecSheetEntry(title='Frame Numbers and Handles', key_list=key_list)
        dialog.exec_()
        # self.fail_check('Check Failed')
