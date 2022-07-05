from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.houdini import alchemy as alc
import hou

class ExportClothRig(PreflightCheck):

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
        file_out = alc.scene_object().copy(context='render',
                                           filename='cloth_rig').path_root
        hou.node('/obj/cloth_rig/').setSelected(True)
        alc.export_selected_nodes(file_out)
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')

