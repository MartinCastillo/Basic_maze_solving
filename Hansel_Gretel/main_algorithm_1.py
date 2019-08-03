#|This is the code which you executate
#___________________________________________________________________________________________|
#|Este codigo implementa el siguente algoritmo:                                             |
#|Asigna un numero 0 a todos los caminos como antes, suma al lugar por el que pase          |
#|un 1 cada vez, simpre va en direción a donde hay un número menor, en  caso de             |
#|haber varias opciones se elige con una prioridad aleatoria, sigue así hasta llegar        |
#|al final, un -1 ,siempre tomará esta opcion pues no puede haber una menor.                |
#___________________________________________________________________________________________|
#|This code implemens the following algorithm:                                              |
#|Assigns a number 0 to all the paths, sums 1 to a block where it passes, choose the path   |
#||with less number, in the case there are several options it chooses with a random priority|
#|the direction, continue like this until it arrives to a -1,it always choose that path.    |
#||Basiclly it remembers the passed paths and avoid them.                                   |
#___________________________________________________________________________________________|
#Global imports
import numpy as np
from matplotlib import pyplot as plt
import cv2
from time import sleep
from random import randint
#Local imports
import gui_algorithm_1

#Global variablesq
screen_size = 500
block_size = 25
cube_margin = 5
delay=100
font_size=2

#nxn matrix for the maze format, 0 is nothing, 999 is wall,-1 is ending
maze_format=np.array(
[[999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999],
 [999,  0,  0,  0,  0,999,  0,  0,  0,999,  0,  0,  0,999,999,999,999,  0,  0,999],
 [999,  0,999,999,  0,999,  0,999,  0,999,  0,999,  0,999,999,999,999,999,  0,999],
 [999,  0,999,  0,  0,999,  0,999,  0,999,  0,999,  0,  0,  0,  0,  0,  0,  0,999],
 [999,  0,999,  0,999,999,  0,999,  0,999,  0,999,  0,999,999,999,999,  0,999,999],
 [999,  0,999,  0,  0,999,  0,999,999,999,  0,999,  0,999,999,999,999,  0,999,999],
 [999,  0,999,999,  0,999,  0,  0,  0,999,  0,999,  0,  0,999, -1,999,  0,999,999],
 [999,  0,999,  0,  0,999,  0,999,  0,999,  0,999,999,999,999,  0,999,  0,999,999],
 [999,  0,999,999,999,999,  0,999,  0,999,  0,999,  0,  0,  0,  0,999,  0,999,999],
 [999,  0,  0,  0,  0,  0,  0,999,  0,999,  0,999,  0,999,999,  0,999,  0,999,999],
 [999,999,999,  0,999,999,  0,999,  0,999,  0,  0,  0,999,999,  0,999,  0,999,999],
 [999,  0,999,  0,  0,999,  0,999,999,999,999,  0,999,999,  0,999,999,  0,999,999],
 [999,  0,999,999,  0,999,  0,  0,  0,999,  0,  0,999,  0,  0,999,999,  0,999,999],
 [999,  0,999,  0,  0,999,  0,999,999,999,999,999,999,999,  0,999,999,  0,999,999],
 [999,  0,999,  0,999,999,  0,999,  0,  0,  0,  0,  0,  0,  0,  0,999,  0,  0,999],
 [999,  0,999,  0,  0,999,  0,999,  0,999,  0,999,999,999,999,  0,  0,  0,999,999],
 [999,  0,999,999,  0,999,  0,999,  0,999,  0,999,999,  0,999,999,999,  0,999,999],
 [999,  0,999,  0,  0,999,  0,999,  0,999,  0,999,  0,  0,  0,999,999,  0,999,999],
 [999,  0,  0,  0,999,999,  0,  0,  0,999,  0,  0,  0,999,  0,  0,999,  0,  0,999],
 [999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999]]
    )
print(maze_format.shape)
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
    current_coord=[12,8] #|initial coordinates
    iters=0
    giros=0
    seleccion=None
    while(True):
            if(maze_format[current_coord[0],current_coord[1]] == -1):
                break
            maze_format[current_coord[0],current_coord[1]] +=1
            ret, map = gui_algorithm_1.draw_map(maze_format,screen_size,block_size,
                corner_text=str(iters),corner_text_size=font_size,corner_text_color=(50,50,200)
                    )
            map = gui_algorithm_1.draw_cube(map,current_coord[0],current_coord[1],
                cube_margin,block_size
                    )
            cv2.imshow('1',map)
            k = cv2.waitKey(delay)
            if(k==ord('q')):
                break
            iters+=1

            #|Analyze surroundings of the cube
            res_matrix=see_laterals(maze_format,current_coord[0],
                current_coord[1]
                    )
            #print(res_matrix)

            #|Goes in the dircetion with less value
            efective = np.array([res_matrix[0,1],res_matrix[1,0],res_matrix[1,2],res_matrix[2,1]])
            min_val = np.min(efective)
            #print(res_matrix)

            #|This loop iterates over the conditions randomly according to a
            #random number, when one of them is fulfilled, regardless of the
            #order, it leaves the loop.
            ultima_direccion=seleccion
            while(True):
                if(randint(0,3)==0) and (min_val == res_matrix[0,1]): #Up
                        current_coord = [current_coord[0]-1,current_coord[1]]
                        direction_register.append({'UP':res_matrix})
                        seleccion=0
                        break
                if(min_val == res_matrix[2,1]): #Dpwn
                        current_coord = [current_coord[0]+1,current_coord[1]]
                        direction_register.append({'DOWN':res_matrix})
                        seleccion=1
                        break
                if(min_val == res_matrix[1,0]): #Right
                        current_coord = [current_coord[0],current_coord[1]-1]
                        direction_register.append({'RIGHT':res_matrix})
                        seleccion=2
                        break
                if(min_val == res_matrix[1,2]): #Left
                        current_coord = [current_coord[0],current_coord[1]+1]
                        direction_register.append({'LEFT':res_matrix})
                        seleccion=3
                        break
            #|Counts the changes of direction
            if(seleccion==ultima_direccion):
                giros += 1
    print('Iters: {}'.format(iters),'---------------------------')
    ret, map = gui_algorithm_1.draw_map(maze_format,screen_size,block_size,corner_text=
        ('{} Steps, {} Turns'.format(str(iters),giros)),corner_text_size=1,
            corner_text_color=(0,0,200))
    map = gui_algorithm_1.draw_cube(map,current_coord[0],current_coord[1],
        cube_margin,block_size
            )
    cv2.imshow('1',map)
    k = cv2.waitKey(0)
    if(k==ord('q')):
        cv2.destroyAllWindows()
    pass
pass
