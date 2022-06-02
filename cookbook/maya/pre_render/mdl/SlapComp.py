from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.nuke import alchemy as alc
# from cgl.plugins.nuke.slap_comp import build_turntable_slapcomp

import getpass


class SlapComp(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Creates a slap comp script for this render
        Submits that slap comp to be rendered.
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
        alc.create_turntable_submission(render_path, parent_job=job_id[0], pool='turntable')
        # alc.create_turntable_submission(source_sequence=render_path,parent_job=job_id[0], pool='turntable')
        # # submit the slap comp to deadline to render.
        # alc.submit_to_farm(sc_info['scene_file'], sc_info['write_node'], sc_info['start_frame'],
        #                    sc_info['end_frame'], sc_info['output_dir'], job_info['job_id'])
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
