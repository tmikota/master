from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya.tasks.mdl import import_references


class ImportReference(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """

        """
        refs = import_references()
        if refs:
            self.pass_check('Check Passed')
        else:
            self.fail_check("Import Failed")
        # self.fail_check('Check Failed')
