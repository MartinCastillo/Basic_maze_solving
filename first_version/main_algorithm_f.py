#__________________________________________________________________________________
#|#En este codigo de prueba se implementa un algoritmo de solución de laberintos  |
#|simple, por cada iteración toma una dirección totalmente aleatoria, luego con_  |
#|sulta si esa dirección esta disponible, si es así va en esa dirección. Si bien  |
#|este algoritmo es simpe, tiene el problema de que le toma (en vase a 12 pruebas)|
#|en promedio 50 iteraciones llegar, y aveces no lo logra pues se atora con el    |
#|propio 'camino' que genera                                                      |
#__________________________________________________________________________________
#|This is the code which you executate
#Global imports
import numpy as np
from matplotlib import pyplot as plt
import cv2
from time import sleep
from random import randint
#Local imports
import gui

#Global variables
start_coord=(8,1)
screen_size = 500
delay = 25
#8x8 matrix for the maze format, 0 is nothing, 1 is wall, 2 is ending,3 extra
maze_format=np.array(
[[1,1,1,1,1,1,1,1,1,1],
 [1,1,1,1,1,1,0,0,2,1],
 [1,1,0,0,1,1,0,1,1,1],
 [1,1,1,0,1,1,0,1,1,1],
 [1,1,1,0,1,1,0,1,1,1],
 [1,0,0,0,0,0,0,1,1,1],
 [1,0,1,1,1,1,1,1,1,1],
 [1,0,1,1,1,1,1,1,1,1],
 [1,0,1,1,1,1,1,1,1,1],
 [1,1,1,1,1,1,1,1,1,1]]
    )
direction_register=[]
#see_laterals function
def see_laterals(maze_format,ycoord,xcoord):
    """
    This function allow you to know the lateral blocks of the cube, it recives
    the map and coordinates of the block and returns the 8 lateral blocs in a
    3x3 matrix in format
    [[n, n, n],
     [n, 0, n],
     [n, n, n]] where n is a 1 or 0 or 2 (1 is wall 0 is no wall, 2 is ending)
                and 0 is an empty space for the shape
    """
    res_matrix = maze_format[ycoord-1:ycoord+2,xcoord-1:xcoord+2]
    return(res_matrix)

if(__name__=='__main__'):
    arrive = False
    current_coord=[8,1] #Coordenadas de inicio
    iters=0

    while(True):
            if(maze_format[current_coord[0],current_coord[1]] == 2):
                break
            maze_format[current_coord[0],current_coord[1]] = 3
            map = gui.draw_map(maze_format,screen_size,corner_text=str(iters))
            map = gui.draw_cube(map,current_coord[0],current_coord[1])
            cv2.imshow('1',map)
            k = cv2.waitKey(delay)
            if(k==ord('q')):
                break
            #print('iters+=1')
            iters+=1

            #Analizar alrededores
            res_matrix=see_laterals(maze_format,current_coord[0],
                current_coord[1]
                    )
            #print(res_matrix)
            direction = randint(-1,2)
            direction_register.append(direction)
            #-1 es abajo 1 es arriba 2 es derecha 0 es izquierda

            if((direction == -1)or(direction == 1)): #Arriba o abajo
                if((maze_format[current_coord[0]-direction,current_coord[1]] == 0) or
                    (maze_format[current_coord[0]-direction,current_coord[1]] == 2)):
                        current_coord=[current_coord[0]-direction,current_coord[1]]
            elif(direction == 0): #izquierda
                if((maze_format[current_coord[0],current_coord[1]-1] == 0)or
                    (maze_format[current_coord[0],current_coord[1]-1] == 2)):
                        current_coord=[current_coord[0],current_coord[1]-1]
            elif(direction == 2): #derecha
                if((maze_format[current_coord[0],current_coord[1]+1] == 0)or
                    (maze_format[current_coord[0],current_coord[1]+1] == 2)):
                        current_coord=[current_coord[0],current_coord[1]+1]
    map = gui.draw_map(maze_format,screen_size,corner_text=(str(iters)+' iteraciones'),
        corner_text_size=1
            )
    map = gui.draw_cube(map,current_coord[0],current_coord[1])
    cv2.imshow('1',map)
    k = cv2.waitKey(0)
    if(k==ord('q')):
        cv2.destroyAllWindows()
    print('Iterations: {}'.format(iters),'---------------------------')
    print('Registro de direcciones: {}'.format(direction_register    ))
    pass
