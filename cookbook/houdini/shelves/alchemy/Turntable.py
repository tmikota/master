import cgl.plugins.houdini.alchemy as alc

def run():
    import hou
    import toolutils
    
    selection = hou.selectedNodes()
    
    viewer = toolutils.sceneViewer()
    view = viewer.curViewport()
    
    root = hou.node('/obj')
    rotationNull = root.createNode('null')
    
    selection[0].setInput(0, rotationNull)
    
    nullYRotation = rotationNull.parm("ry")
    
    key1 = hou.Keyframe()
    key1.setFrame(1)
    key1.setValue(0)
    
    nullYRotation.setKeyframe(key1)
    
    key2 = hou.Keyframe()
    key2.setFrame(240)
    key2.setValue(360)
    
    nullYRotation.setKeyframe(key2)
    
    geometry = selection[0].renderNode().geometry()
    bbox = geometry.boundingBox()
    
    camera = root.createNode("cam")

    camYPosition = camera.parm("ty")
    camZPosition = camera.parm("tz")
    camYPosition.set(bbox.center()[1])
    camZPosition.set((bbox.sizevec()[1])*2.4)

    view.setCamera(camera)
    hou.ui.triggerUpdate()
    
    root.layoutChildren()

