import pymel.core as pm
import maya.mel as mel


def get_items(item_name):
    str_items = []
    items = pm.ls(regex='\w+:\w{}\w*\d*:mdl'.format(item_name))
    for i in items:
        str_items.append(str(i))
    return str_items


def key_all_visibility(items, visibility=0, frame=pm.currentTime(query=True)):
    for item in items:
        pm.setAttr('{}.visibility'.format(item), visibility)
        pm.animation.setKeyframe(item, v=visibility, t=frame, itt='linear', ott='linear', at='visibility')


def show_this(this, the_rest, frame):
    key_all_visibility([this], visibility=1, frame=frame)
    key_all_visibility(the_rest, visibility=0, frame=frame)


def process_this(this, all_, i):
    i += 1
    pm.currentTime(i, edit=True)
    hidden = all_.copy()
    hidden.remove(this)
    show_this(this, hidden, i)
    return i


def hide_all(chest_items, back_items, head_items, mask_items, eyes_items, frame):
    key_all_visibility(chest_items, 0, frame)
    key_all_visibility(back_items, 0, frame)
    key_all_visibility(head_items, 0, frame)
    key_all_visibility(mask_items, 0, frame)
    key_all_visibility(eyes_items, 0, frame)


def reset_visibility():
    pm.currentTime(1)
    mdls = pm.ls(regex='*:mdl')
    for mdl in mdls:
        mel.eval('CBdeleteConnection "{}.v";'.format(mdl))


def run():
    """
    Creates all the asset variants within the scene
    """
    reset_visibility()
    pm.select(d=True)
    chest_items = get_items('Chest')
    back_items = get_items('Back')
    noggin_items = get_items('Noggin')
    head_items = get_items('Head')
    mask_items = get_items('Mask')
    eyes_items = get_items('Eyes')
    i = 0
    hide_all(chest_items, back_items, head_items, mask_items, eyes_items, i)
    pm.currentTime(i, edit=True)
    for noggin in noggin_items:
        i = process_this(noggin, noggin_items, i)
        key_all_visibility(eyes_items, visibility=0, frame=i)
        key_all_visibility(head_items, visibility=0, frame=i)
        key_all_visibility(chest_items, visibility=0, frame=i)
        key_all_visibility(back_items, visibility=0, frame=i)
        key_all_visibility(mask_items, visibility=0, frame=i)
        for chest in chest_items:
            i = process_this(chest, chest_items, i)
            key_all_visibility(eyes_items, visibility=0, frame=i)
            key_all_visibility(head_items, visibility=0, frame=i)
            key_all_visibility(back_items, visibility=0, frame=i)
            key_all_visibility(mask_items, visibility=0, frame=i)
            for back in back_items:
                i = process_this(back, back_items, i)
                key_all_visibility(eyes_items, visibility=0, frame=i)
                key_all_visibility(head_items, visibility=0, frame=i)
                key_all_visibility(mask_items, visibility=0, frame=i)
                for head in head_items:
                    i = process_this(head, head_items, i)
                    key_all_visibility(eyes_items, visibility=0, frame=i)
                    key_all_visibility(mask_items, visibility=0, frame=i)
                    for eyes in eyes_items:
                        i = process_this(eyes, eyes_items, i)
                        key_all_visibility(mask_items, visibility=0, frame=i)
                        for mask in mask_items:
                            i = process_this(mask, mask_items, i)
    # set end frame to whatevr i is.
    pm.playbackOptions(animationStartTime=1, minTime=1,
                       maxTime=i, animationEndTime=i)


