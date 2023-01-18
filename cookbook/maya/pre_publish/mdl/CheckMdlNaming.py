from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.maya.tasks.mdl as mdl
import cgl.plugins.maya.tools.renamer.ui as ui


class CheckMdlNaming(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Checks complete model heirarchy for proper naming conventions
        """
        if mdl.check_mdl_naming():
            self.pass_check('Check Mdl Naming')
        else:
            self.fail_check('Model Naming Failed, run Model Renamer')
            this = ui.ModelRenamer()
            this.exec_()

