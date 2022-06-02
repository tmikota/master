from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya.alchemy import scene_object


class ExportShader(PreflightCheck):

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
        import pymel.core as pm
        import maya.mel as mel
        mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
        so = scene_object()
        pub_path = so.copy(context='render', name='shaders').path_root
        if pub_path.endswith('_shd.mb'):
            pub_path = pub_path.replace('_shd.mb', '_shd_shaders.mb')
        sel = pm.ls(type='shadingEngine')
        count = 0
        exclude = ['initialShadingGroup', 'initialParticleSE']
        for x in sel:
            if x not in exclude:
                if count == 0:
                    pm.select(x, r=True, ne=True)
                else:
                    pm.select(x, tgl=True, ne=True)
                count += 1
        print('Exporting %s' % pub_path)
        pm.exportSelected(pub_path, typ='mayaBinary')
        self.pass_check('Shader Exported to: %s' % pub_path)
