from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.maya import alchemy as alc
from cgl.plugins.project_management.shotgun.utils import get_framerange
from cgl.plugins.maya.tasks.cam import set_frame_range
import maya.cmds as cmds


class SetFrameRange(PreflightCheck):

    def run(self):
        """
        sets the frame range based on shotgrid start end frames
        """

        scene_object = alc.scene_object()
        frame_start, frame_end = get_framerange(scene_object).split('-')
        cmds.playbackOptions(animationStartTime=frame_start, animationEndTime=frame_end)
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
