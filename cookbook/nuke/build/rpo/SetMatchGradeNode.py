from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.nuke.progress import Progress, ProgressAbort
import threading
from PySide2 import QtCore
import time
import nuke

# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.nuke import alchemy as alc


class SetMatchGradeNode(PreflightCheck):
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
        print("Match Transforms to Edit Ref")

        # TODO: check shotgun for a flag set by editorial indicating if the repo is static or dynamic (animated)
        #       Defaulting to True. User can cancel progress if not required.

        is_animated = True

        _autoalign_thread = MatchTransformsThreaded(is_animated)
        _autoalign_thread.start()

        self.pass_check("Check Passed")


class MatchTransformsThreaded(threading.Thread):
    """Create an update thread with a progress bar to update nuke after advancing each frame"""
    
    def __init__(self, is_animated=True):
        """
        Initialize the Auto-align thread.

        If is_animated is true, each frame gets calculated and keyframes are saved to the transform_REPO node.

        Args:
            is_animated (bool): If True, the repo is keyframed on each frame, otherwise the value is set but not keyed.
        """
        threading.Thread.__init__(self)
        self.is_animated = is_animated
        self.progress = None
        self.frame = nuke.frame()
        self.plate_node = nuke.toNode('read_PLATE')
        self.first_frame = self.plate_node['first'].value()
        self.last_frame = self.plate_node['last'].value()
        # EDIT_REF_NODE = nuke.toNode('read_EREF')
        self.match_grade_node = nuke.toNode('matchgrade_REPO')
        self.match_grade_node.showControlPanel()
        self.match_grade_translation = None
        self.match_grade_scale = None

        self.repo_node = nuke.toNode('transform_REPO')
        self.repo_translate_curve_y = None
        self.repo_translate_curve_x = None
        self.repo_scale_curve_x = None
        self.repo_scale_curve_y = None
        self.viewer_data = {}

        if self.is_animated:
            self.repo_node['translate'].setAnimated()
            self.repo_node['scale'].setAnimated()
            self.repo_translate_curve_x = self.repo_node['translate'].animation(0)
            self.repo_translate_curve_y = self.repo_node['translate'].animation(1)
            self.repo_scale_curve_x = self.repo_node['scale'].animation(0)
            self.repo_scale_curve_y = self.repo_node['scale'].animation(1)

    def __get_repo_transforms(self):
        self.match_grade_translation = self.match_grade_node['translation'].value()
        self.match_grade_scale = self.match_grade_node['scale'].value()
        
    def __set_keyframe(self):
        tx, ty = self.match_grade_translation
        sx, sy = self.match_grade_scale

        self.repo_translate_curve_x.setKey(self.frame, tx)
        self.repo_translate_curve_y.setKey(self.frame, ty)
        self.repo_scale_curve_x.setKey(self.frame, sx)
        self.repo_scale_curve_y.setKey(self.frame, sy)
    
    def __set_value(self):
        self.repo_node['translate'].setValue(self.match_grade_translation)
        self.repo_node['scale'].setValue(self.match_grade_scale)

    def __disconnect_viewers(self):
        """
        gets info about all the viewers and their connections, then disconnects them
        """
        for viewer in nuke.allNodes('Viewer'):
            self.viewer_data[viewer.name()] = {'deps': viewer.dependencies(), 'node': viewer}
            for index, v in enumerate(viewer.dependencies()):
                viewer.setInput(index, None)
        return

    def __reconnect_viewers(self):
        """
        takes a dict of viewer connections and reconnects them
        """
        for viewer_name in self.viewer_data:
            viewer = self.viewer_data[viewer_name]['node']
            for index, d in enumerate(self.viewer_data[viewer_name]['deps']):
                viewer.setInput(index, d)
        return

    def run(self):
        """
        Override thread's run function to spawn calls to the main nuke thread. This allows updates mid-process.
        
        progress bar handling is wrapped in try/except/finally to avoid hanging nuke if user cancels, raising ProgressAbort
        
        Disconnects viewer to speed up processing.
        """
        nuke.executeInMainThreadWithResult(self.__disconnect_viewers)
        if self.is_animated:   # nuke.executeInMainThreadWithResult(nuke.ask, 'Match All Frames? (slow)\n\nYes = Keyframe all frames\nNo = Single frame'):
            # Loop over all frames, setting keys on the repo transform node after the auto-alignment
            self.progress = Progress(amount=1, name='Aligning All Frames', enable=True)
            try:
                self.progress.set_message("Keyframe Repo")
                self.progress.add_amount(self.last_frame-self.first_frame+1)

                for _frame in range(self.first_frame, self.last_frame+1):
                    if self.progress.is_abort():
                        raise ProgressAbort
                    self.frame = _frame
                    self.progress.set_message(f"Go To {self.frame}")
                    nuke.executeInMainThreadWithResult(nuke.frame, args=self.frame)
                    time.sleep(.02)
                    self.progress.set_message(f"Align To {self.frame}")
                    nuke.executeInMainThreadWithResult(self.match_grade_node['autoAlign'].execute)
                    time.sleep(.02)
                    self.progress.set_message(f"Keyframe {self.frame}")
                    nuke.executeInMainThreadWithResult(self.__get_repo_transforms)
                    time.sleep(.02)
                    nuke.executeInMainThreadWithResult(self.__set_keyframe)
                    time.sleep(.02)
                    self.progress.update_progress()
            except ProgressAbort:
                print("Cancelled Auto-Alignment")
            except Exception as err:
                import traceback
                traceback.print_exc()
                raise err
            finally:
                self.progress.complete()
                del self.progress
        else:
            self.progress = Progress(amount=1, name='Aligning To Middle Frame', enable=True)
            try:
                self.progress.add_amount(3)
                cur_frame = self.frame
                middle_frame = self.first_frame + ((self.last_frame-self.first_frame)/2.0)
                self.frame = middle_frame
                self.progress.set_message(f"Go To {middle_frame}")
                nuke.executeInMainThreadWithResult(nuke.frame, args=self.frame)
                if self.progress.is_abort():
                    raise ProgressAbort
                self.progress.update_progress()
                self.progress.set_message(f"Align to {middle_frame}")
                nuke.executeInMainThreadWithResult(self.match_grade_node['autoAlign'].execute)
                if self.progress.is_abort():
                    raise ProgressAbort
                self.progress.update_progress()
                self.progress.set_message(f"Update transform_REPO")
                nuke.executeInMainThreadWithResult(self.__get_repo_transforms)
                nuke.executeInMainThreadWithResult(self.__set_value)
                self.progress.update_progress()
                self.progress.set_message(f"Return to {cur_frame}")
                nuke.executeInMainThreadWithResult(nuke.frame, args=cur_frame)
                self.progress.update_progress()
            except ProgressAbort:
                print("Auto-Alignment Cancelled By User")
            except Exception as err:
                import traceback
                traceback.print_exc()
                raise err
            finally:
                self.progress.complete()
                del self.progress
                
        nuke.executeInMainThreadWithResult(self.__reconnect_viewers)
