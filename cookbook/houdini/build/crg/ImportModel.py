from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.houdini.tasks.mdl as mdl


class ImportModel(PreflightCheck):
    def getName(self):
        pass

    def run(self):
        """
        Imports the latest published model.
        """
        mdl.Task().import_latest()
        self.pass_check("Check Passed")
        # self.fail_check('Check Failed')
