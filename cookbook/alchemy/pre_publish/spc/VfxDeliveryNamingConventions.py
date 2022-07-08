from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.alchemy.tasks.spc as spc


class VfxDeliveryNamingConventions(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        All details needed for patterns to do with VFX Deliveries.
        """
        try:
            path_object = self.shared_data['path_object']
            key_list = ["Shots Naming Pattern", "Shots Naming Regex", "Trailer Naming Pattern", "Trailer Naming Regex",
                        "Assets Naming Pattern", "Assets Naming Regex"]
            dialog = spc.SpecSheetEntry(title='Frame Numbers and Handles', key_list=key_list, path_object=path_object)
            dialog.exec_()
        except RuntimeError:
            self.fail_check("Check Failed: {}".format(RuntimeError.args))

        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
