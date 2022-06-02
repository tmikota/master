from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya.tasks import mdl



class ExportHighRes(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        export high res obj, fbx, mb files.
        :return:
        """
        types = ['fbx', 'ma', 'abc']
        for t in types:
            mdl.export_mdl(ext=t)
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
