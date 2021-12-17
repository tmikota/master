import pymel.core as pm


def get_items(item_name):
    str_items = []
    items = pm.ls(regex='\w+:\w{}\w:mdl'.format(item_name))
    for i in items:
        str_items.append(str(i))
    return str_items


def key_all_visibility(items, visibility=0, frame=pm.currentTime(query=True)):
    for item in items:
        print('Setting Visibility of {} to {} for frame {}'.format(item, visibility, frame))
        pm.setAttr('{}.visibility'.format(item), visibility)
        pm.animation.setKeyframe(item, v=visibility, t=frame, itt='linear', ott='linear', at='visibility')


def show_this(this, the_rest, frame):
    key_all_visibility([this], visibility=1, frame=frame)
    key_all_visibility(the_rest, visibility=0, frame=frame)


def process_this(this, all, i):
    i += 1
    pm.currentTime(i, edit=True)
    hidden = all.copy()
    hidden.remove(this)
    show_this(this, hidden, i)
    return i


def hide_all(chest_items, back_items, head_items, mask_items, eyes_items, frame):
    key_all_visibility(chest_items, 0, frame)
    key_all_visibility(back_items, 0, frame)
    key_all_visibility(head_items, 0, frame)
    key_all_visibility(mask_items, 0, frame)
    key_all_visibility(eyes_items, 0, frame)


def run():
    """
    Creates all the asset variants within the scene
    """
    pm.select(d=True)
    chest_items = get_items('Chest')
    back_items = get_items('Back')
    noggin_items = get_items('Noggin')
    head_items = get_items('Head')
    mask_items = get_items('Mask')
    eyes_items = get_items('Eyes')
    print('{} total combinations'.format(len(chest_items) * len(back_items) * len(head_items) * len(mask_items)))
    i = 1
    hide_all(chest_items, back_items, head_items, mask_items, eyes_items, i)
    pm.currentTime(i, edit=True)
    for chest in chest_items:
        i = process_this(chest, chest_items, i)
        for noggin in noggin_items:
            i = process_this(noggin, noggin_items, i)
            for back in back_items:
                i = process_this(back, back_items, i)
                for head in head_items:
                    i = process_this(head, head_items, i)
                    for eyes in eyes_items:
                        i = process_this(eyes, eyes_items, i)
                        for mask in mask_items:
                            i = process_this(mask, mask_items, i)
                            if len(mask_items) == 1:
                                i += 1
                                pm.currentTime(i, edit=True)
                                key_all_visibility([mask], visibility=0, frame=i)
        i += 1
        hide_all(chest_items, back_items, head_items, mask_items, eyes_items, i)


