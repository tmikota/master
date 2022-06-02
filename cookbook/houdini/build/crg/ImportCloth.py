from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.houdini.tasks.cth as cth

class ImportCloth(PreflightCheck):
    def getName(self):
        pass

    def run(self):
        """
        imports the latest published "cloth" task.
        :return:
        """
        cth.Task().import_latest()
        print("PreflightTemplate")
        self.pass_check("Check Passed")
        # self.fail_check('Check Failed')
