#!/usr/bin/env python3
"""
Main program and scene setup
"""
# Python built-in modules
import sys

# External, non built-in modules
import glfw                         # lean window system wrapper for OpenGL

from keyframe import KeyFrameControlNode
from loaders import load, load_textured
from skybox import Skybox
from transform import vec, quaternion, quaternion_from_euler
from viewer import Viewer
from node import Node

class Cylinder(Node):
    """ Very simple cylinder based on practical 2 load function """
    def __init__(self):
        super().__init__()
        self.add(*load('./res/cylinder.obj'))  # just load the cylinder from file

def main():
    """ create a window, add scene objects, then run rendering loop """
    viewer = Viewer()

    # place instances of our basic objects
    if len(sys.argv) < 2:
        print('Usage:\n\t%s [3dfile]*\n\n3dfile\t\t the filename of a model in'
              ' format supported by pyassimp.' % (sys.argv[0],))
    
    #translate_keys = {0: vec(0, 0, 0), 10: vec(1, 0, 0), 15: vec(0, 1, 0), 20: vec(0, 0, 1), 25: vec(0, 0, 0)}
    translate_keys = {0: vec(0.75, 0, -1)} 
    # rotate_keys = {0: quaternion(), 2: quaternion_from_euler(180, 0, 180),
    #                4: quaternion_from_euler(180, 0, 180), 6: quaternion()}
    rotate_keys = {0: quaternion()}
    #scale_keys = {0: 0.125, 2: 0.25, 4: 0.5}
    scale_keys = {0: 0.5}
    keynode = KeyFrameControlNode(translate_keys, rotate_keys, scale_keys)
    keynode.add(*[mesh for file in sys.argv[1:] for mesh in load_textured(file)])
    viewer.add(keynode)
    #viewer.add(Cylinder())
    #txt = TexturedPlane('resources/grass.png')
    #viewer.add(txt)

    #viewer.add(*[mesh for file in sys.argv[1:] for mesh in load_textured(file)])
    sea = [
        'res/skybox/right.jpg',
        'res/skybox/left.jpg',
        'res/skybox/top.jpg',
        'res/skybox/bottom.jpg',
        'res/skybox/front.jpg',
        'res/skybox/back.jpg'
    ]
    moonwaw = [
        'res/mp_moonwaw/moonwaw_lf.tga',
        'res/mp_moonwaw/moonwaw_rt.tga',
        'res/mp_moonwaw/moonwaw_up.tga',
        'res/mp_moonwaw/moonwaw_dn.tga',
        'res/mp_moonwaw/moonwaw_ft.tga',
        'res/mp_moonwaw/moonwaw_bk.tga']
    blood_valley = [
        'res/mp_bloodvalley/blood-valley_lf.tga',
        'res/mp_bloodvalley/blood-valley_rt.tga',
        'res/mp_bloodvalley/blood-valley_up.tga',
        'res/mp_bloodvalley/blood-valley_dn.tga',
        'res/mp_bloodvalley/blood-valley_ft.tga',
        'res/mp_bloodvalley/blood-valley_bk.tga']
    viewer.add(Skybox(blood_valley))
    # start rendering loop
    viewer.run()


if __name__ == '__main__':
    glfw.init()                # initialize window system glfw
    main()                     # main function keeps variables locally scoped
    glfw.terminate()           # destroy all glfw windows and GL contexts
