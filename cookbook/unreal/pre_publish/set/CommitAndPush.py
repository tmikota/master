from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.perforce.perforce import commit, push
from cgl.core.utils.general import load_json
from cgl.core.path import PathObject
import unreal
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.unreal import alchemy as alc


class CommitAndPush(PreflightCheck):

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
        filepath = unreal.SystemLibrary.convert_to_absolute_path(unreal.Paths.project_dir())
        project_name = unreal.Paths.get_base_filename(unreal.Paths.get_project_file_path())
        msd_path = filepath + project_name + ".msd"
        source_path = load_json(msd_path)['source_path']
        path_object = PathObject(source_path)
        commit()
        push()
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
