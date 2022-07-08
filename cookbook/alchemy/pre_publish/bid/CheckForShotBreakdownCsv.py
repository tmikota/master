from cgl.plugins.preflight.preflight_check import PreflightCheck
import os


class CheckForShotBreakdownCsv(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Checks for the INTERNAL_SHOT_BREAKDOWN" csv file in the render folder.
        :return:
        """
        po = self.shared_data['path_object']
        ro = po.copy(context='render', filename='INTERNAL_SHOT_BREAKDOWN', ext='csv')
        if os.path.exists(ro.path_root):
            self.shared_data['internal_shot_breakdown'] = ro.path_root
            self.pass_check('Check Passed')
        else:
            self.fail_check('No .csv file found at: {}'.format(ro.path_root))
