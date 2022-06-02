from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.maya import alchemy as alc
from cgl.plugins.maya import utils
from cgl.plugins.maya.tasks import mdl
from importlib import reload
reload(mdl)
reload(utils)
import re


class CheckMtlNames(PreflightCheck):

    def run(self):
        scene_object = alc.scene_object()
        regex = re.compile(r'%s' % scene_object.cfg.project_config['rules']['general']['model_material']['example'])
        example = scene_object.cfg.project_config['rules']['general']['model_material']['example']
        bad_materials, _ = mdl.check_model_children_names()
        if bad_materials:
            dialog = utils.RenameDialog(title="Bad Material Names", regex=regex, name_example=example,
                                       list_items=bad_materials)

            dialog.exec_()
            self.fail_check('Bad material Names')
        else:
            self.pass_check('Materials Named Properly')
