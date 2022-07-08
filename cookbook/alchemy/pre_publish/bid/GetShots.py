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

        save_object = ro.copy(filename='prod_showSetup_bid', ext='json')
        json_path = save_object.path_root

        # TODO - We need a test to ensure the stuff in the bid matches what's in shotgrid as a first step we'll
        # put them in by hand based off what's in the bids we're testing.
        full_dict = {}
        all_shots_dict = {}
        shot_tasks = ['TRACKING', 'LAYOUT', 'ANIMATION', 'CROWDS', 'CFX', 'FX', 'ENVIRO', 'LIGHTING',
                      'DMP', 'COMP PAINT', 'COMP ROTO', 'COMP']
        df = pd.read_csv(csv_file)
        for i in range(len(df)):
            shot_dict = {}
            shot_name = str(df.loc[i]['SHOT NUMBER'])
            scope_of_work = str(df.loc[i]['SCOPE OF WORK'])
            notes = str(df.loc[0]['NOTES'])
            shot_dict['Scope of Work'] = scope_of_work
            shot_dict["Notes"] = notes
            shot_dict['tasks'] = {}
            for each in shot_tasks:
                try:
                    value = int(df.loc[i][each])
                    if value > 0:
                        shot_dict['tasks'][each] = value
                except ValueError:
                    pass
            all_shots_dict[shot_name] = shot_dict
        full_dict["Shots"] = all_shots_dict
        save_json(filepath=json_path, data=full_dict)
        self.pass_check("Check Passed")
