from cgl.plugins.preflight.preflight_check import PreflightCheck

# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.nuke import alchemy as alc
from cgl.plugins.project_management.shotgun.utils import get_framerange


class SetFrameRange(PreflightCheck):
    def getName(self):
        pass

    def run(self):
        """
        script to be executed when the preflight is run.

        If the preflight is successful:
        self.pass_check('Message about a passed Check')

        if the preflight fails:
        self.fail_check('Message about a failed check')
        :return:
        """
        import nuke
        import traceback
        po = alc.scene_object()
        try:
            start, end = get_framerange(po).split('-')
        except Exception as err:
            traceback.print_exc()
            self.fail_check(f'Check Failed. Could not find frame in and frame on on shotgrid.\n'
                            f'Refer to script editor for more details')
            return

        if not start.isnumeric() or not end.isnumeric():
            self.fail_check('Check Failed. Could not find start frame or end frame on shotgrid ')
            return

        root = nuke.root()
        root['first_frame'].setValue(int(start))
        root['last_frame'].setValue(int(end))
        self.pass_check('frame start and end set ')
