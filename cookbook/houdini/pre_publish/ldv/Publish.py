
from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.houdini import alchemy as alc


class Publish(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        alc.save_file()

        render_po = alc.scene_object().copy(context = 'render')
        
        shutil.copyfile(alc.scene_object().path_root, render_po.path_root)
        
        if os.path.isfile(render_po.path_root):
            self.pass_check('Check Passed')
        else:
            self.fail_check('Check Failed')

