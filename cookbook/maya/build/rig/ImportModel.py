from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.maya.tasks import mdl
import cgl.plugins.maya.alchemy as alc

class ImportModel(PreflightCheck):
    def getName(self):
        pass

    def run(self):
        """
        pass
        """
        print("PreflightTemplate")
        # self.fail_check('Check Failed')

        filepath = alc.scene_object().copy(task='mdl',user = 'publish',latest = True, set_proper_filename = True, ext = '.ma', context = 'render')
        mdl.Task()._import(filepath.path_root,reference =False)
        self.pass_check("Check Passed")
