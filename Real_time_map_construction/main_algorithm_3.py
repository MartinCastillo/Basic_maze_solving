#En proceso


#Global imports
import numpy as np
from matplotlib import pyplot as plt
import cv2
from time import sleep
from random import randint

#Local imports
import gui_algorithm_3
from class_robot import Robot,r

#Global variables
screen_size = 500
block_size = 25
cube_margin = 5
delay=100#delay entre frames
font_size=2
#El 1 indica la posición local de la izquierda del robot
initial_orientation = [0 ,0,0,1]

#nxn matrix for the maze format, 0 is nothing in the place, 999 is wall,-1 is ending
#The robot cant acces to this information, only throgth the lateral blocks
maze_format=np.array(
[[999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999],
 [999,  0,  0,  0,  0,999,  0,  0,  0,999,  0,  0,  0,999,999,999,999,999,999,999],
 [999,  0,999,999,  0,999,  0,999,  0,999,  0,999,  0,999,999,999,999,999,999,999],
 [999,  0,999,  0,  0,999,  0,999,  0,999,  0,999,  0,999,999,999,999,999,999,999],
 [999,  0,999,  0,999,999,  0,999,  0,999,  0,999,  0,999,999,999,999,999,999,999],
 [999,  0,999,  0,  0,999,  0,999,  0,999,  0,999,  0,999,999,999,999,999,999,999],
 [999,  0,999,999,  0,999,  0,999,  0,999,  0,999,  0,  0,999, -1,999,999,999,999],
 [999,  0,999,  0,  0,999,  0,999,  0,999,  0,999,999,999,999,  0,999,999,999,999],
 [999,  0,999,999,999,999,  0,999,  0,999,  0,999,  0,  0,  0,  0,999,999,999,999],
 [999,  0,  0,  0,  0,  0,  0,999,  0,  0,  0,999,  0,999,999,  0,999,999,999,999],
 [999,999,999,999,999,999,  0,999,999,999,  0,  0,  0,999,999,  0,999,999,999,999],
 [999,999,999,999,999,999,  0,999,999,999,999,999,999,999,999,999,999,999,999,999],
 [999,999,999,999,999,999,  0,  0,  0,999,999,999,999,999,999,999,999,999,999,999],
 [999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999],
 [999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999],
 [999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999],
 [999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999],
 [999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999],
 [999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999],
 [999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999]]
    )
action_register=[]

if(__name__=='__main__'):
    robot = Robot(initial_orientation,[12,8])
    registro_de_acciones = []
    while(True):
        #Si llegas
        if(maze_format[robot.current_coord[0],robot.current_coord[1]] == -1):
            break

        #robot.avanza(maze_format)
        #robot.gira_derecha()
        #robot.gira_izquierda()
        #Aquí se puede hacer un ciclo del robot, puede realizar las Acciones
        #anteriores, y acceder a la informacion de res matrix
        ####################################################################
        ####################################################################
        #Analizar alrededores, res matrix es la unica informacion del entorno
        #(maze_format)que puede recibir, si se quiere orientar, va a tener
        #que hacerlo con un mapa inerno
        percepcion=robot.see_laterals(maze_format)
        #percepcion es un lista de 4 elementos [izquierda,adelante,derecha,atras]

        print(percepcion)
        robot.avanzar(maze_format)
        #Detectar cruces
        if(percepcion.count(0)>1):
            registro_de_acciones.append(robot.current_coord,)
            robot.avanzar(maze_format)

        robot.gira_derecha()
        robot.avanzar(maze_format)
        ####################################################################
        ####################################################################
        #Dibuja en pantalla
        ret, map = gui_algorithm_3.draw_map(maze_format,screen_size,block_size,
            corner_text=str('text'),corner_text_size=font_size,corner_text_color=(100,100,255)
                )
        map = gui_algorithm_3.draw_cube(map,robot.current_coord[0],robot.current_coord[1],
            robot._local,cube_margin,block_size
                )
        cv2.imshow('1',map)
        k = cv2.waitKey(delay)
        if(k==ord('q')):
            break
    #Terimna programa#
    cv2.imshow('1',map)
    k = cv2.waitKey(0)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        print('Acciones: {}'.format(action_register),'---------------------------')
    pass
