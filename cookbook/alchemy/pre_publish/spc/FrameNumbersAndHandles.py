from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.alchemy.tasks.spc as spc


class FrameNumbersAndHandles(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Get speck sheet info around frame numbers and handles.
        """
        key_list = ['First Delivered Frame', 'First Frame', 'First Cut Frame', 'Ingest Handles', 'Delivery Handles']
        dialog = spc.SpecSheetEntry(title='Frame Numbers and Handles', key_list=key_list)
        dialog.exec_()
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
