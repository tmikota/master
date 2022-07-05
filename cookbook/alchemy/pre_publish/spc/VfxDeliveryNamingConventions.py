from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.alchemy.tasks.spc as spc


class VfxDeliveryNamingConventions(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        All details needed for patterns to do with VFX Deliveries.
        """
        key_list = ["Shots Naming Pattern", "Shots Naming Regex", "Trailer Naming Pattern", "Trailer Naming Regex",
                    "Assets Naming Pattern", "Assets Naming Regex"]
        dialog = spc.SpecSheetEntry(title='Frame Numbers and Handles', key_list=key_list)
        dialog.exec_()
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
