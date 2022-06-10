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
        msd_info = tex.Task(path_object=po).export_msd()
        mtl_groups = sorted(msd_info['attrs']['mtl_groups'])
        self.shared_data['tex_mtl_groups'] = mtl_groups
        self.pass_check('Check Passed')
