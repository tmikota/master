from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya import alchemy as alc
import pymel.core as pm


class ExportRig(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        rig_object = alc.scene_object().copy(context='render')
        rig_export_path = rig_object.path_root
        if pm.objExists('rig'):
            pm.select('rig')
            # pm.exportSelected(rig_export_path, typ='mayaBinary')
            pm.exportSelected(rig_export_path, constraints=True, expressions=True, shader=True, type='mayaBinary',
                              constructionHistory=True, channels=True)
            self.pass_check("Rig has been published")
        else:
            self.fail_check("Could Not Find 'rig' in the scene")
