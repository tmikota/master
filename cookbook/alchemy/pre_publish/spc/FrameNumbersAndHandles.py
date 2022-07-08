from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.alchemy.tasks.spc as spc


class FrameNumbersAndHandles(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Get speck sheet info around frame numbers and handles.
        """
        try:
            path_object = self.shared_data['path_object']
            key_list = ['First Delivered Frame', 'First Frame', 'First Cut Frame', 'Ingest Handles', 'Delivery Handles']
            dialog = spc.SpecSheetEntry(title='Frame Numbers and Handles', key_list=key_list, path_object=path_object)
            dialog.exec_()
        except RuntimeError:
            self.fail_check("Check Failed: {}".format(RuntimeError.args))

        self.pass_check("Check Passed")
