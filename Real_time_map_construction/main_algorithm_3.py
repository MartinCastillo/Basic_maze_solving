#El objetivo es simular lo que sería la construcción de mapas en tiempo real,

#Global imports
import numpy as np
from matplotlib import pyplot as plt
import cv2
from time import sleep
from random import randint
#Local imports
import gui_algorithm_3

gui = True
#Global variablesq
screen_size = 500
#Parte de la gui
block_size = 25
cube_margin = 5
delay=100
font_size=2

#nxn matrix for the maze format, 0 is nothing, 999 is wall,-1 is ending
#Intentamos simular un ambiente para que el 'robot' pueda explorar,moverse
maze_format=np.array(
[[999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999],
 [999,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
 [999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
 [999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999]]
    )
#Para hacerlo a escala hacemos una medida de los cuadros
medida_cuadro = 18#cm
tamanno_mapa = [maze_format.shape[0]*medida_cuadro,maze_format.shape[1]*medida_cuadro]
#Es el mapa actual que va a empezar a rellenar
map = np.array([])
#Es la posición inicial del robot, que es 0,0 , según se mueva va cambiando
posicion = [0,0]

direction_register=[]
#see_laterals function
def see_laterals(maze_format,ycoord,xcoord):
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

if(__name__=='__main__'):
    arrive = False
    current_coord=np.array([12,8])*medida_cuadro #Local coords, in the 'word'
    print(tamanno_mapa,current_coord)
    iters=0
    giros=0
    seleccion=None
    while(True):

        arrive = True
        if (arrive):
            break
pass
