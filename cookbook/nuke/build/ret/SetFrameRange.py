from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.nuke import alchemy as alc

from cgl.plugins.project_management.shotgun.utils import get_framerange


class SetFrameRange(PreflightCheck):
    def run(self):
        import nuke
        # figure out why i'm creating a ton of shots and no versions.
        # 'frame_range' is the field we'll be querying.



        po = alc.scene_object()
        start, end = get_framerange(po).split('-')

        if not start or not end:
            self.fail_check('could not find frame in and frame on on shotgrid ')

        root = nuke.root()
        root['first_frame'].setValue(int(start))
        root['last_frame'].setValue(int(end))
        self.pass_check('frame start and end set ')

