##Apenas comenzando

#Global imports
import numpy as np
import cv2
from time import sleep
from random import randint
#Local imports
from  gui_algorithm_3 import Gui
from class_robot import Robot
#Global variablesq
screen_size = 500
block_size = 25
cube_margin = 5
delay=100
font_size=2
#nxn matrix for the maze format, 0 is nothing, 999 is wall,-1 is ending
#Es una representacion del mundo, cada cuadro representa cierta distancia,se
#supone que son de 15x15
maze_format=np.array(
[[999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999],
 [999,  0,999,  0,  0,999,  0,  0,  0,999,  0,  0,  0,999,999,999,999,  0,  0,999],
 [999,  0,999,999,  0,  0,  0,999,  0,999,  0,999,  0,999,999,999,999,999,  0,999],
 [999,  0,999,  0,  0,999,  0,999,  0,999,  0,999,  0,  0,  0,  0,  0,  0,  0,999],
 [999,  0,999,  0,999,999,  0,999,  0,999,  0,999,  0,999,999,999,999,  0,999,999],
 [999,  0,  0,  0,  0,  0,  0,999,999,999,  0,999,  0,999,999,999,999,  0,999,999],
 [999,  0,999,999,  0,999,  0,  0,  0,999,  0,999,  0,  0,999, -1,999,  0,999,999],
 [999,  0,999,  0,  0,999,  0,999,  0,  0,  0,999,999,999,999,  0,999,  0,999,999],
 [999,  0,999,999,999,999,  0,999,  0,999,  0,999,  0,  0,  0,  0,999,  0,999,999],
 [999,  0,  0,  0,  0,  0,  0,999,  0,999,  0,999,  0,999,999,  0,999,  0,999,999],
 [999,999,999,  0,999,999,  0,999,  0,999,  0,  0,  0,999,999,  0,999,  0,999,999],
 [999,  0,999,  0,  0,999,  0,999,999,999,999,  0,999,999,  0,999,999,  0,999,999],
 [999,  0,999,999,  0,999,  0,  0,  0,999,  0,  0,999,  0,  0,999,999,  0,999,999],
 [999,  0,999,  0,  0,999,  0,999,999,999,999,999,999,999,999,999,999,  0,999,999],
 [999,  0,999,  0,999,999,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,999,  0,  0,999],
 [999,  0,999,  0,  0,999,  0,999,  0,999,  0,999,999,999,999,  0,  0,  0,999,999],
 [999,  0,999,999,  0,999,  0,999,  0,  0,  0,999,999,  0,999,999,999,  0,999,999],
 [999,  0,999,  0,  0,999,  0,999,  0,999,  0,999,  0,  0,  0,999,999,  0,999,999],
 [999,  0,  0,  0,999,999,  0,  0,  0,999,  0,  0,  0,999,  0,  0,999,  0,  0,999],
 [999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999]]
    )

#Almacena las esquinas y la dirección que toma
direction_register=[]
#see_laterals function
if(__name__=='__main__'):
    iters=0; giros=0
    arrive = False
    current_coord=[1,1] #|initial coordinates
    medida_cuadro = 15
    seleccion=None
    #clases instance
    gui = Gui(screen_size)
    robot = Robot([10,10],medida_cuadro)
    while(True):
            #Condicion si llega
            if(maze_format[current_coord[0],current_coord[1]] == -1):
                break
            """Dibuja mapa"""
            maze_format[current_coord[0],current_coord[1]] +=1
            ret, map = gui.draw_map(maze_format,screen_size,block_size,
                corner_text=str(iters),corner_text_size=font_size,corner_text_color=(50,50,200)
                    )
            """Dibuja robot"""
            map = gui.draw_cube(map,current_coord[0],current_coord[1],
                cube_margin,block_size
                    )
            cv2.imshow('1',map)
            k = cv2.waitKey(delay)
            if(k==ord('q')):
                break
            iters+=1

            """Ve si hay paredes en los alrrededores"""
            #|Analyze surroundings of the cube
            res_matrix=robot.see_laterals(maze_format,current_coord[0],
                current_coord[1]
                    )

            #|Goes in the dircetion with less value
            #efective es un array de 1x4 con las paredes
            efective = np.array([res_matrix[0,1],res_matrix[1,0],res_matrix[1,2],res_matrix[2,1]])
            min_val = np.min(efective)
            print(min_val)

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
                if(randint(0,3)==1) and (min_val == res_matrix[2,1]): #Dpwn
                        current_coord = [current_coord[0]+1,current_coord[1]]
                        direction_register.append({'DOWN':res_matrix})
                        seleccion=1
                        break
                if(randint(0,3)==2) and (min_val == res_matrix[1,0]): #Right
                        current_coord = [current_coord[0],current_coord[1]-1]
                        direction_register.append({'RIGHT':res_matrix})
                        seleccion=2
                        break
                if(randint(0,3)==3) and (min_val == res_matrix[1,2]): #Left
                        current_coord = [current_coord[0],current_coord[1]+1]
                        direction_register.append({'LEFT':res_matrix})
                        seleccion=3
                        break

            #|Counts the changes of direction
            if(seleccion==ultima_direccion):
                giros += 1
    print('Iters: {}'.format(iters),'---------------------------')
    ret, map = gui.draw_map(maze_format,screen_size,block_size,corner_text=
        ('{} Steps, {} Turns'.format(str(iters),giros)),corner_text_size=1,
            corner_text_color=(0,0,200))
    map = gui.draw_cube(map,current_coord[0],current_coord[1],
        cube_margin,block_size
            )
    cv2.imshow('1',map)
    k = cv2.waitKey(0)
    if(k==ord('q')):
        cv2.destroyAllWindows()
    pass
pass
