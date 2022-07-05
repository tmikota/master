from cgl.plugins.preflight.preflight_check import PreflightCheck

# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.nuke import alchemy as alc
from cgl.plugins.project_management.shotgun.utils import get_resolution


class SetResolution(PreflightCheck):
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
        print("PreflightTemplate")
        import nuke
        import traceback
        po = alc.scene_object()
        try:
            resolution = get_resolution(po)
        except Exception as err:
            traceback.print_exc()
            self.fail_check(f'Check Failed. Could not find resolution on on shotgrid.\n'
                            f'Refer to script editor for more details')
            return
        if not resolution:
            self.fail_check('Check Failed.Could not find resolution on on shotgrid')
            return
        _format = '{} 1'.format(resolution.replace('x', ' '))
        format_obj = nuke.addFormat(_format)  # We need a format obj not just a str

        root = nuke.root()
        root['format'].setValue(format_obj)
        self.pass_check('Check Passed Resolution, set')
