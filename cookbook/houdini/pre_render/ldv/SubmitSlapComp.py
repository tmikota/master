from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.nuke import alchemy as alc


class SubmitSlapComp(PreflightCheck):

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
        parent_job_id = job_info['job_id']
        print('parent_job_id::', parent_job_id)

        # # build a slap comp for the shot
        # sc_info = build_turntable_slapcomp(render_path)
        job_id = alc.create_turntable_submission(render_path, parent_job=parent_job_id[0], pool='turntable')
        # alc.create_turntable_submission(source_sequence=render_path,parent_job=job_id[0], pool='turntable')
        # # submit the slap comp to deadline to render.
        # alc.submit_to_farm(sc_info['scene_file'], sc_info['write_node'], sc_info['start_frame'],
        #                    sc_info['end_frame'], sc_info['output_dir'], job_info['job_id'])
        if job_id:
            self.pass_check('Check Passed')
        else:
            self.fail_check('Check Failed')
