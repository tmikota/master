from cgl.plugins.preflight.preflight_check import PreflightCheck
import pymel.core as pm
import os
from cgl.plugins.maya.alchemy import scene_object
from cgl.core.utils.general import save_json


class Rarity(PreflightCheck):

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
        pm.currentTime(1)
        mdls = pm.ls(regex='*:mdl')
        eframe = int(pm.playbackOptions(query=True, animationEndTime=True))
        i = int(pm.playbackOptions(query=True, animationStartTime=True))
        path_object = scene_object().copy(context='render')
        export_dir = os.path.dirname(path_object.path_root)
        filename = path_object.filename_base
        #print(uuid.uuid5(uuid.NAMESPACE_URL, path_object.filename_base))

        while i < eframe:
            i += 1
            attrs = []
            dict = {}
            pm.currentTime(i)
            for mdl in mdls:
                if not 'femaleA:mdl' in str(mdl):

                    pm.select(mdl)
                    pm.pickWalk(d='up')
                    trait = pm.ls(sl=True)[0].split(':')[-1]
                    value_name = str(mdl).split(":")[1]
                    if pm.getAttr('{}.visibility'.format(mdl)):
                        attrs.append({"value": value_name,
                                      "trait": trait})
            frame_num_string = "{0:04d}".format(i)
            json_filename = "{}.{}.json".format(filename, frame_num_string)
            source_filename = json_filename.replace('.json', '.png')
            dict['name'] = ""
            dict['description'] = ""
            dict['image'] = ""
            dict['dna'] = os.path.join(export_dir, source_filename)
            dict['edition'] = 1
            dict['date'] = ""
            dict['attributes'] = attrs
            full_json_path = os.path.join(export_dir, json_filename)
            save_json(full_json_path, dict)
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
