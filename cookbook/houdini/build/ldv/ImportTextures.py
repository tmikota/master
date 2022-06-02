from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.houdini.tasks.tex as tex
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.houdini import alchemy as alc


class ImportTextures(PreflightCheck):
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
        tex.Task().import_latest()
        self.pass_check("Check Passed")
        # self.fail_check('Check Failed')
