

def run():
    import cgl.plugins.maya.alchemy as alc

    so = alc.scene_object()
    anim_o = so.copy(context='render', task='anim', user='publish', latest=True,
                     filename='{}_{}_anim.mb'.format(so.seq, so.shot))
    print(anim_o.path_root)

    alc.reference_file(anim_o.path_root)
