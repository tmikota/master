from cgl.plugins.preflight.preflight_check import PreflightCheck
import os
import re
from cgl.core.utils.general import cgl_move


class OrganizeTexFiles(PreflightCheck):

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
        po = self.shared_data['path_object']
        po = po.copy()
        if os.path.isfile(po.path_root) or '##' in po.filename:
            render_dir = os.path.dirname(po.copy(context='render').path_root).replace('*', '')
        else:
            render_dir = po.copy(context='render').path_root
        regex = r'[a-z]+_mtl'
        for file in os.listdir(render_dir):
            filepath = os.path.join(render_dir, file)
            if os.path.isfile(filepath):
                match = re.search(regex, file)
                if match:
                    mtl_group = match.group()
                    dest = os.path.join(render_dir, mtl_group, file)
                    cgl_move(filepath, dest)
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
