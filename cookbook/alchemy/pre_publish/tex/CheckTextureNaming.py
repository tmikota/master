from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.alchemy.tasks.tex import ConfirmPublishFiles
from cgl.core.path import PathObject
from cgl.core.utils.general import cgl_move
import os
import re
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.alchemy import alchemy as alc


class CheckTextureNaming(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Runs a Texture Naming Check Dialog to ensure textures are properly sorted before a publish.
        :return:
        """
        # po = PathObject(r'V:/COMPANIES/marz/render/ocra/master/assets/char/kamala/tex/default/tmikota/000.000/high')
        # # po = self.shared_data['path_object']
        dialog = ConfirmPublishFiles(path_object=self.shared_data['path_object'])
        dialog.exec_()
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')


if __name__ == '__main__':
    po = PathObject(r'V:/COMPANIES/marz/render/ocra/master/assets/char/kamala/tex/default/tmikota/000.000/high')
    render_dir = po.path_root
    regex = r'[a-z]+_mtl'
    print(render_dir)
    for file in os.listdir(render_dir):
        filepath = os.path.join(render_dir, file)
        if os.path.isfile(filepath):
            match = re.search(regex, file)
            mtl_group = match.group()
            mtl_group = mtl_group.replace('_mtl', '')
            dest = os.path.join(render_dir, mtl_group, file)
            cgl_move(filepath, dest)



