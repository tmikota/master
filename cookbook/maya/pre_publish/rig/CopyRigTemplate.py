from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.maya import alchemy as alc
from cgl.core.path import PathObject
import os
import shutil

class CopyRigTemplate(PreflightCheck):


    def get_folders_from_source(self):
        source_dir = alc.scene_object().copy(filename='')
        directories = os.listdir(source_dir.path_root)

        path_object_directories = []

        for dir in directories:
            path = os.path.join(source_dir.path_root, dir)
            if os.path.isdir(path):
                po = PathObject(path)
                path_object_directories.append(po)

        return path_object_directories

    def run(self):
        """
        script to be executed when the preflight is run.

        If the preflight is successful:
        self.pass_check('Message about a passed Check')

        if the preflight fails:
        self.fail_check('Message about a failed check')
        :return:
        """
        rig_templates = self.get_folders_from_source()
        for dir in rig_templates:
            source = dir.path_root
            render = dir.copy(context='render').path_root
            shutil.copytree(source, render)
        self.pass_check('Rig Templates copied ')
        # self.fail_check('Check Failed')



