from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.project_management.shotgun.utils import get_resolution
from cgl.plugins.nuke import alchemy as alc
import nuke


class SetResolution(PreflightCheck):

    def run(self):
        po = alc.scene_object()
        resolution = get_resolution(po)
        if not resolution:
            self.fail_check('Check Failed. Check Script Editor for errors')
        _format = '{} 1'.format(resolution.replace('x', ' '))
        format_obj = nuke.addFormat(_format)  # We need a format obj not just a str

        root = nuke.root()
        root['format'].setValue(format_obj)
        self.pass_check('Check Passed Resolution, set')
