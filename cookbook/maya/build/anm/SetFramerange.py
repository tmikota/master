from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.maya.tasks import cam
from cgl.core.path import PathObject

class SetFramerange(PreflightCheck):
    def getName(self):
        pass

    def run(self):
        """

        :return:
        """
        print("setting framerange")
        cam_import = cam.Task()

        latest_cam = PathObject(cam.get_latest())
        msd_info = latest_cam.msd_info
        
        start_frame = msd_info['attrs']['start_frame']
        end_frame = msd_info['attrs']['end_frame']
        handle_start = msd_info['attrs']['handle_start']
        handle_end = msd_info['attrs']['handle_end']
        
        cam.set_frame_range(start_frame,end_frame,handle_start,handle_end)

        self.pass_check("Check Passed")
        # self.fail_check('Check Failed')
