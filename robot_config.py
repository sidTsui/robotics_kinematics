###Sidney Tsui
###Lab3-robot kinematics
###problem 2
###2/13/24
###purpose: test robot_models

import math
import numpy as np
import robot_model

###use to test code:
### a1 = 1
### a2 = 1
### 01 = pi/2
### 02 = pi/2
def two_link():

    #slide 33
    link = np.array([[math.pi / 2, 1, 0, 0], [math.pi / 2, 1, 0, 0]])#formats b, a, d, c

    trans = robot_model.kinematic_chain(link)#calls kinematic chain
    x, y, z = robot_model.get_pos(trans)#get position from matrix results
    roll, pitch, yaw = robot_model.get_rot(trans)#get orientation from matrix results

    #prints results as formatted on assignment sheet
    print("x =", "{:.2f}".format(x), "meter")
    print("y =", "{:.2f}".format(y), "meter")
    print("z =", "{:.2f}".format(z), "meters")
    print("roll =", "{:.2f}".format(roll), "radians")
    print("pitch =", "{:.2f}".format(pitch), "radians")
    print("yaw =", "{:.2f}".format(yaw), "radians")

    print("")

    return x, y, z, roll, pitch, yaw

def Case1():
    ##slide 37
    DHparams = ([0, 0, 0.1625, math.pi/2], [0, -0.425, 0, 0], [0, -0.3922, 0, 0], [0, 0, 0.1333, math.pi/2], [0, 0, 0.0997, -math.pi/2], [0, 0, 0.0996, 0])
    trans = robot_model.kinematic_chain(DHparams)
    x, y, z = robot_model.get_pos(trans)
    roll, pitch, yaw = robot_model.get_rot(trans)

    #prints results as formatted on assignment sheet
    print("x =", "{:.2f}".format(x), "meter")
    print("y =", "{:.2f}".format(y), "meter")
    print("z =", "{:.2f}".format(z), "meters")
    print("roll =", "{:.2f}".format(roll), "radians")
    print("pitch =", "{:.2f}".format(pitch), "radians")
    print("yaw =", "{:.2f}".format(yaw), "radians")
    print("")

    return x, y, z, roll, pitch, yaw

def Case2():
    ##slide 37
    DHparams = ([0, 0, 0.1625, math.pi/2], [-math.pi/2, -0.425, 0, 0], [0, -0.3922, 0, 0], [0, 0, 0.1333, math.pi/2], [0, 0, 0.0997, -math.pi/2], [0, 0, 0.0996, 0])
    trans = robot_model.kinematic_chain(DHparams)
    x, y, z = robot_model.get_pos(trans)
    roll, pitch, yaw = robot_model.get_rot(trans)

    #prints results as formatted on assignment sheet
    print("x =", "{:.2f}".format(x), "meter")
    print("y =", "{:.2f}".format(y), "meter")
    print("z =", "{:.2f}".format(z), "meters")
    print("roll =", "{:.2f}".format(roll), "radians")
    print("pitch =", "{:.2f}".format(pitch), "radians")
    print("yaw =", "{:.2f}".format(yaw), "radians")

    return x, y, z, roll, pitch, yaw

#calling functions to test
two_link()
Case1()
Case2()
