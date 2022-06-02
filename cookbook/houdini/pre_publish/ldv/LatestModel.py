# from cgl.plugins.houdini import alchemy as alc
import os
from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.core.path import PathObject
import hou 


class LatestModel(PreflightCheck):


    def run(self):
        """
        make sure we have the latest model in houdini, if not replace the path with the latest model.
        """
        print('PreflightTemplate')

        parm = hou.parm('/obj/char_kamala_mdl/abc/fileName')#TODO: replace with top node 
        path = parm.eval().replace('\\','/')
        po = PathObject(path)
        latest_version = po.copy(user = 'publish').latest_version().path_root

        if not path == latest_version : 
            parm.set(latest_version)
        if os.path.isfile(latest_version):
            self.pass_check('Check Passed')
        else: 
            self.fail_check('Check Failed')
