#En proceso


#For more easy code design.This class represent a robot, it only can get the info
#from the envrioment that a robot would get, and return an action, forward, turn,rigth
#turn left, backwards.
#The envrioment can get all the robot's physical information
import numpy as np
class Robot:
    def __init__(self,robot_shape,initial_position):
        self.robot_shape = robot_shape
        self.orientacion = []
        self.position = np.array(initial_position)#Coorditates from the staring point
        #always start in the left bottom corner

    def see_laterals(self,maze_format,ycoord,xcoord):
        res_matrix = maze_format[ycoord-1:ycoord+2,xcoord-1:xcoord+2]
        top distance
        return(res_matrix)
