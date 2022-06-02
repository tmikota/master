from cgl.plugins.preflight.preflight_check import PreflightCheck
import os
import cgl.plugins.houdini.alchemy as alc
from cgl.core.utils.general import save_json, load_json
from cgl.core.path import PathObject
from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.houdini import alchemy as alc
import hou 

class LatestTextures(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        query all textures and ensure they are the latest published version of the texture.  If not throw a popup.  Ensure absolute paths,
        """
        print('PreflightTemplate')
        # self.pass_check('Check Passed')
        # self.fail_check('Check Failed')

        # Fetches the latest texture publish
        po = alc.scene_object().copy(task='tex', latest=True, user='publish', set_proper_filename=True)
        
        tex_msd_path = po.msd_path
        msd_dict = load_json(tex_msd_path)
        shading_dict = msd_dict['attrs']
        mtl_group = shading_dict['mtl_groups'] # List of all the material groups from MSD
        
        for mat in hou.node('/mat').children():
            mtl_group = '{}_mtl'.format(mat)
            for node in hou.node('/mat/{}'.format(mat)).children():
                if node.type().name() == 'redshift::TextureSampler':
                    current_file = node.parm('tex0').eval()  # Value of Texture Map path
                    msd_file = shading_dict[mtl_group][node.name()]['png']
                    if current_file != msd_file:
                        self.fail_check('Check Failed')
        
        self.pass_check('Check Passed')