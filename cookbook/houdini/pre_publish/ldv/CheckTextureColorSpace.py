from cgl.plugins.preflight.preflight_check import PreflightCheck
import hou
import cgl.plugins.houdini.alchemy as alc


class CheckTextureColorSpace(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        For each texture, check to ensure the color space is correct based off the shader.json file.
        """
        so = alc.scene_object()
        project_color_space = so.project_settings['working_colorspace']

        for mat in hou.node('/mat').children():
            for node in hou.node('/mat/{}'.format(mat)).children():
                if node.type().name() == 'redshift::TextureSampler':
                    current_color_space = node.parm('tex0_colorSpace').eval()
                    if current_color_space == '':
                        current_color_space = 'auto'
                    if current_color_space != project_color_space:
                        self.fail_check('Check Failed: please check texture on the material {} inside the texture node {}'.format(mat.name(),node.name()))

        self.pass_check('Check Passed')