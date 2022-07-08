from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.three_d_equalizer import alchemy as alc
# from cgl.plugins.nuke import alchemy as alc
from cgl.plugins.three_d_equalizer.tasks.trk import export_nuke
from cgl.core.path import lj_list_dir
import os


class Exportnuke(PreflightCheck):

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
        check_passed = False
        nuke_file = None
        try:
            nuke_file = export_nuke()
            print('EXPORTED nuke_file:::', nuke_file)
        except RuntimeError:
            self.fail_check("Runtime Error: {}".format(RuntimeError.args))
        try:
            from rez_utils import rez_utils
            out, err = rez_utils.run_rez_subprocess(rez_packages=['nuke', 'alchemy', '3DE_LDPK'],
                                                    commands=['nuke', '-t',
                                                              rf'{os.environ["REZ_ALCHEMY_ROOT"]}\python\cglumberjack\cgl\plugins\nuke\tasks\trk.py',
                                                              'build-3de-lens-distort-nuke-file',
                                                              '--exported_nuke_file', nuke_file,
                                                              '--output_variant', 'undistort',
                                                              '--deadline_submit', 'True']
                                                    )
            print("err:::", err)
            print("out:::", out)
            outlines = out.splitlines()
            new_nuke_file = None
            for line in outlines:
                if 'Nuke Build Completed -->' in line:
                    new_nuke_file = line.split('-->')[1].strip()
                    break
            if not os.path.isfile(new_nuke_file):
                self.fail_check('Check Failed,Nuke file not completed')
            else:
                # so = alc.scene_object()
                # po = so.copy(task="plt", user="publish", latest=True, context="render", set_proper_filename=True,
                #              ext="")
                # dirname = os.path.dirname(po.path_root)
                # dir_list = lj_list_dir(dirname)
                # frame_range = dir_list[0].split(" ")[1]
                # frange_split = frame_range.split("-")
                # start_frame = int(frange_split[0])
                # end_frame = int(frange_split[1])
                check_passed = True
        except RuntimeError:
            self.fail_check("Runtime Error: {}".format(RuntimeError.args))
        if check_passed:
            self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
