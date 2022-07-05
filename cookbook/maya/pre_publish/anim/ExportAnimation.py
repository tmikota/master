from cgl.plugins.preflight.preflight_check import PreflightCheck

from cgl.plugins.maya import alchemy as alc
from cgl.plugins.maya.tasks import anim_export
import maya.cmds as cmds
from cgl.plugins.project_management.shotgun.utils import get_framerange


class ExportAnimation(PreflightCheck):

    def run(self):
        print('PreflightTemplate')
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')


    for rig_name in cmds.ls('*:rig'):
        char_exp = anim_export.CharacterAnimationExporter()
        scene_object = alc.scene_object()
        json_export = scene_object.copy(context='render',
                                        filename='{}_{}_{}_{}.json'.format(scene_object.seq,
                                                                           scene_object.shot,
                                                                           scene_object.task,
                                                                           rig_name.split(':')[0]))

        abc_export = json_export.copy(ext='abc')
        json_path = json_export.path_root
        directory = os.path.dirname(json_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        abc_path = abc_export.path_root

        frame_start, frame_end = get_framerange(scene_object).split('-')

        char_exp.add_character(rig_name,
                               start=int(frame_start),
                               end=int(frame_end),
                               increment=1.0,
                               keyframe_file_path=json_path,
                               abc_file_path=abc_path)

        char_exp.export_all()
