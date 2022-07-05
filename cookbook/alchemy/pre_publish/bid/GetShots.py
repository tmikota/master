from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.core.path import PathObject
import pandas as pd
import os
from cgl.core.utils.general import save_json


class GetShots(PreflightCheck):

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
        ro = po.copy(context='render', filename='INTERNAL_SHOT_BREAKDOWN', ext='csv')
        csv_file = ro.path_root
        shot_dict = {}
        # TODO - We need a test to ensure the stuff in the bid matches what's in shotgrid as a first step we'll
        # put them in by hand based off what's in the bids we're testing.
        shot_tasks = ['TRACKING', 'LAYOUT', 'ANIMATION', 'CROWDS', 'CFX', 'FX', 'ENVIRO', 'LIGHTING',
                      'DMP', 'COMP PAINT', 'COMP ROTO', 'COMP']
        # df = pd.read_excel(sheet, sheet_name, engine='openpyxl')
        df = pd.read_csv(csv_file)
        for i in range(len(df)):
            shot_name = str(df.loc[i]['SHOT NUMBER'])
            shot_dict[shot_name] = {}
            for each in shot_tasks:
                try:
                    value = int(df.loc[i][each])
                    if value:
                        shot_dict[shot_name][each] = "True"
                    else:
                        shot_dict[shot_name][each] = "False"
                except ValueError:
                    pass
        # TODO: Throw up a GUI showing off what we'll be building in Shotgrid.
        if shot_dict:
            json_path = ro.copy(set_proper_filename=True, ext='json').path_root
            save_json(json_path, shot_dict)
            self.pass_check('shot breakdown json file created: {}'.format(json_path))
        else:
            self.fail_check("Check Failed - invalid csv data for shots")

