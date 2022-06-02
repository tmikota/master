from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.houdini import alchemy as alc
import hou 

class CheckShaderUtilAovs(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Checks to ensure all required shader AOVS are in the shader.
        """
        so = alc.scene_object()
        
        for mat in hou.node('/mat').children():
            maps = []
            for node in hou.node('/mat/{}'.format(mat)).children():
                if node.type().name() == 'redshift::TextureSampler':
                    maps.append(node.name())
            if not maps.__contains__("BaseColor"):
                self.fail_check('Check Failed: Missing BaseColor in {}'.format(mat.name()))
            if not maps.__contains__("Normal"):
                self.fail_check('Check Failed: Missing Normal in {}'.format(mat.name()))
            if not maps.__contains__("Roughness"):
                self.fail_check('Check Failed: Missing Roughness in {}'.format(mat.name()))
        
        self.pass_check('Check Passed')
