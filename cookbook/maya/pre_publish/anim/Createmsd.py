from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.maya.tasks.anim as anim
reload(anim)


class Createmsd(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
       
        """
        anim.Task().export_msd(self.shared_data['publish_object'])
        self.pass_check('Animation msd created')
