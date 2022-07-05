from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.maya import alchemy as alc
import pymel.core as pm
import os 

class ExportRig(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        rig_object = alc.scene_object().copy(context='render')
        rig_export_path = rig_object.path_root
        directory = os.path.dirname(rig_export_path)
        
        if not os.path.exists(directory):
            os.makedirs(directory)
        if pm.objExists('rig'):
            pm.select('rig')
            pm.exportSelected(rig_export_path, constraints=True, expressions=True, shader=True, type='mayaAscii',
                              force=True, preserveReferences=True,
                              constructionHistory=True, channels=True)
            self.pass_check("Rig has been published")
        else:
            self.fail_check("Could Not Find 'rig' in the scene")


