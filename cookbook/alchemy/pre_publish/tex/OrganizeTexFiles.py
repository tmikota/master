from cgl.plugins.preflight.preflight_check import PreflightCheck
import os
import re
from cgl.core.utils.general import cgl_move
from cgl.plugins.maya.tasks.tex import organize_tex_folder

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
        organize_tex_folder(po)
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
