from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya.tasks import tex


class CreateMsd(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Creates an MSD file for the texture task.
        :return:
        """
        po = self.shared_data['path_object']
        tex.Task(path_object=po).export_msd()
        self.pass_check('Check Passed')