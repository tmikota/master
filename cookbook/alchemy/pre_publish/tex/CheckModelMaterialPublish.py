from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.maya.tasks import tex
from cgl.core.path import PathObject

class CheckModelMaterialPublish(PreflightCheck):

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
        mo = po.copy(latest=True, task='mdl', user='publish', set_proper_filename=True, ext='ma')
        print(sorted(po.msd_info['attrs']['mtl_groups']))
        print(mo.msd_info['attrs']['mtl_groups'])
        tex_mtl_groups = sorted(po.msd_info['attrs']['mtl_groups'])
        mdl_mtl_groups = sorted(mo.msd_info['attrs']['mtl_groups'])

        if tex_mtl_groups == mdl_mtl_groups:
            self.pass_check('Material Groups Match!')
        else:
            self.fail_check('Material Groups do not Match!')
            print(tex_mtl_groups)
            print(mdl_mtl_groups)


