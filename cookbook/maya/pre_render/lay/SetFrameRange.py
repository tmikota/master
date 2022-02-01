from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.ui.widgets.dialog import InputDialog
import pymel.core as pm
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.maya import alchemy as alc


class SetFrameRange(PreflightCheck):

    def getName(self):
        pass

    @staticmethod
    def set_frame_range(start_frame, end_frame, handle_start, handle_end):
        print('setting playback options {} {} {} {}'.format(handle_start, start_frame, end_frame, handle_end))
        pm.playbackOptions(animationStartTime=handle_start, minTime=start_frame,
                           maxTime=end_frame, animationEndTime=handle_end)

    def run(self):
        """
        script to be executed when the preflight is run.

        If the preflight is successful:
        self.pass_check('Message about a passed Check')

        if the preflight fails:
        self.fail_check('Message about a failed check')
        :return:
        """
        sframe = int(pm.playbackOptions(query=True, animationStartTime=True))
        eframe = int(pm.playbackOptions(query=True, animationEndTime=True))
        dialog_ = InputDialog(title='Set Frame Range', message='Enter Frame Range (example: 1-500)', line_edit=True,
                              line_edit_text="{}-{}".format(sframe, eframe))
        dialog_.exec()
        if dialog_.button == 'Ok':
            if '-' in dialog_.input_text:
                sframe, eframe = dialog_.input_text.split('-')
                pm.setAttr("defaultRenderGlobals.fs", int(sframe))
                pm.setAttr("defaultRenderGlobals.ef", int(eframe))
                self.set_frame_range(sframe, eframe, sframe, eframe)
        self.pass_check('Check Passed')
