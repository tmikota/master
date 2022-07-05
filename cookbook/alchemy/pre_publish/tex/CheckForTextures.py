from cgl.plugins.preflight.preflight_check import PreflightCheck
import os
from cgl.core.path import lj_list_dir


class CheckForTextures(PreflightCheck):

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
        so = self.shared_data['path_object']
        po = so.copy(context='render')
        if not po.path_root.endswith(po.resolution):
            render_dir = os.path.dirname(po.path_root)
        else:
            render_dir = po.path_root
        exrs = []
        for root, dirs, files in os.walk(render_dir):
            for name in files:
                if name.endswith('exr'):
                    exrs.append(name)
        if not exrs:
            self.fail_check('No exr files found in render directory, check fails.')
            return
        self.pass_check('Found {} exr files, check passed'.format(len(exrs)))
