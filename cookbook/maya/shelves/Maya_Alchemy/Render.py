import cgl.plugins.maya.alchemy as alc


def run():
    so = alc.scene_object()
    alc.render(preview=False, cam='turntable_camera1')



