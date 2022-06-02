from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.maya import alchemy as alc
from cgl.plugins.nuke import alchemy as alc

import getpass

class SlapComp(PreflightCheck):

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
        job_info = self.shared_data['job_info']
        print('job_info::', job_info)
        render_path = job_info['render_path']
        # job = job_info['job']
        # print('job::',job)
        job_id = job_info['job_id']
        print('job_id::', job_id)

        # # build a slap comp for the shot
        # sc_info = build_turntable_slapcomp(render_path)
        alc.create_turntable_submission(parent_job=job_id[0], source_sequence=render_path)
        # # submit the slap comp to deadline to render.
        # alc.submit_to_farm(sc_info['scene_file'], sc_info['write_node'], sc_info['start_frame'],
        #                    sc_info['end_frame'], sc_info['output_dir'], job_info['job_id'])
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')

