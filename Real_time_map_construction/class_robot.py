#For more easy code design.This class represent a robot, it only can get the info
#from the envrioment that a robot would get, and return an action, forward, turn,rigth
#turn left, backwards.
#The envrioment can get all the robot's physical information
import numpy as np
class Robot:
    def __init__(self,robot_shape,medida_cuadro):
        self.robot_shape = robot_shape
        self.orientacion = []
        self.position = np.array([12,8])*medida_cuadro #Local coords, in the 'word'    def see_laterals(maze_format,coords):

    def see_laterals(self,maze_format,ycoord,xcoord):
        """
        This function allow you to know the lateral blocks of the cube, it recives
        the map and coordinates of the block and returns the 8 lateral blocks in a
        3x3 matrix in format
        [[n, n, n],
         [n, 0, n],
         [n, n, n]]
        where n is a number (0 is no wall, 999 is wall, other number
        is a passed path)
        """
        res_matrix = maze_format[ycoord-1:ycoord+2,xcoord-1:xcoord+2]
        return(res_matrix)
