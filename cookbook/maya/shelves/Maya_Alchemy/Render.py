import cgl.plugins.maya.alchemy as alc


def run():
    so = alc.scene_object()
    real_render = ['lite', 'shd', 'comp']
    if so.task in real_render:
        alc.render(preview=False, cam='turntable_camera1')
    else:
        alc.render(preview=True, cam='turntable_camera1')


