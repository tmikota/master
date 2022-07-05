from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.houdini import alchemy as alc
from cgl.plugins.houdini import set_aov as aov

class SumbitToDeadline(PreflightCheck):

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
        # lte_layers = ['CHAR', 'FG', 'BG','MG','FX','PRP','VEH','UTL']
        try:
            rop_list = aov.get_rops()
            job_info = []
            if not rop_list:
                aov.set_rops()
                rop_list = aov.get_rops()
            for rop in rop_list:
                job_info.append(alc.submit_to_farm(node_name=rop.path(), pool='redshift_houdini', layer=rop.name()))
        except:
            print('Error')
            job_info = alc.submit_to_farm()

        self.shared_data['job_info'] = job_info
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
