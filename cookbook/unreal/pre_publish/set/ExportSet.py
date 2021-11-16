from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.unreal_engine.utils import export_selected_set
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.unreal import alchemy as alc


class ExportSet(PreflightCheck):

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
        print('PreflightTemplate')
        
        path_object = export_selected_set()
        path_object.publish()
        self.pass_check('Check Passed: Exported {} and published {}'.format(path_object.path_root, "path_to_publish"))
        # self.fail_check('Check Failed')
