###Sidney Tsui
###Lab3-robot kinematics
###problem 1
###2/13/24

import math
import numpy as np 


###this function:
#######receives the Denavit-Hartenberg parameters
#######returns a combined homogenous transformation according to this convention.
def dh_transformation(a, b, c, d):
	##b = theta
	##c = alpha
	##receiving denavit-hartenberg params
	dhtrans = np.array([[math.cos(b), (-(math.sin(b))*(math.cos(c))), math.sin(b)* math.sin(c), a*math.cos(b)],
			    [math.sin(b), math.cos(b) * math.cos(c),  (-(math.cos(b))*(math.sin(c))), a*math.sin(b)],
			    [0.0,math.sin(c), math.cos(c), d],
			    [0.0,0.0,0.0,1.0]
				])
	#returns combined homogeneous trans
	return dhtrans
	
	
###this function:
#######receives a 2D list/array containing the DH parameters of a robotic manipulator and returns a homogenous transformation for the kinematic chain
def kinematic_chain(twoDlist):
	trans = np.array([[]])
	###set up a loop that scans the rows and multiplies the transformation 	to get a total transformation.
	
###this function:
#######eceives a homogeneous transformation as input and returns the x, y, z components of the position.
def get_pos(H):
	###positions received from assignment sheet
	x = H[0][3] ##h14
	y = H[1][3] ##h24
	z = H[2][3] ##h34
	
	return x, y, z
	

###this function:
#######eceives a homogeneous transformation as input and returns roll-pith-yaw angles 
def get_rot(trans):
	##formulas on assignment sheet
	roll_rot = math.atan2(trans[2][1], trans[2][2])
	pitch_rot = math.atan2((-(trans[2][0])), math.sqrt(((trans[2][1])**2) + ((trans[2][2])**2)
	yaw_rot = math.atan2(trans[1][0], trans[0][0])
	###order for rotational motion in assignment sheet
	
	return roll_rot, pitch_rot, yaw_rot
