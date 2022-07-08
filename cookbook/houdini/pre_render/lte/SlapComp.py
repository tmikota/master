from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.nuke import alchemy as alc

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
        for job in job_info:
            render_path = job['render_path']
            # job = job_info['job']
            # print('job::',job)
            parent_job_id = job['job_id']
            job_id = alc.create_turntable_submission(render_path, parent_job=parent_job_id[0])
            print('parent_job_id::', parent_job_id)
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
