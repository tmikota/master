import cgl.plugins.houdini.alchemy as alc

def run():
    import hou
    import toolutils
    
    selection = hou.selectedNodes()
    
    viewer = toolutils.sceneViewer()
    view = viewer.curViewport()
    scene = alc.scene_object()
    frame_length = int(scene.project_settings['turntable_length'])
    root = hou.node('/obj')
    rotationNull = root.createNode('null')
    
    selection[0].setInput(0, rotationNull)
    
    nullYRotation = rotationNull.parm("ry")
    
    key1 = hou.Keyframe()
    key1.setFrame(1)
    key1.setValue(0)
    
    nullYRotation.setKeyframe(key1)
    
    key2 = hou.Keyframe()
    key2.setFrame(frame_length)
    key2.setValue(360)
    
    nullYRotation.setKeyframe(key2)
    
    selectedGeoNode = selection[0]
    geometry = selectedGeoNode.renderNode().geometry()
    bbox = geometry.boundingBox()
    
    camera = root.createNode("cam")
    
    outsideScale = selectedGeoNode.parm("scale").eval()
    
    camYPosition = camera.parm("ty")
    camZPosition = camera.parm("tz")
    
    if bbox.sizevec()[0] < bbox.sizevec()[1]:
        camYPosition.set(bbox.center()[1]*outsideScale)
        camZPosition.set((bbox.sizevec()[1])*2.6*outsideScale)
    else:
        camYPosition.set(bbox.center()[1]*outsideScale)
        camZPosition.set((bbox.sizevec()[0])*2.2*outsideScale)
    
    view.setCamera(camera)
    hou.ui.triggerUpdate()
    
    root.layoutChildren()
