from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.maya.alchemy as alc
from cgl.plugins.maya.tasks.lite import get_render_folder
import pymel.core as pm
import os


class SetUpPaths(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Sets the render output path to the alchemy default
        :return:
        """

        ro = alc.scene_object().copy(context='render')
        render_dir = os.path.dirname(ro.path_root)
        pm.workspace(fileRule=['images', render_dir])
        self.pass_check('Images Path Set to {}'.format(ro.path_root))
