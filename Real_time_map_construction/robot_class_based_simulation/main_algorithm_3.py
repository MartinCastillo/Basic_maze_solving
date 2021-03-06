#En proceso


#Global imports
import numpy as np
from matplotlib import pyplot as plt
import cv2
from time import sleep
from random import randint
from maze_mapping.maze_mapping import Mapping_tools

#Local imports
import gui_algorithm_3
from class_robot import Robot,r

#Global variables
screen_size = 500
block_size = 25
cube_margin = 5
delay=200#delay entre frames
font_size=2
visualizar = True
#El 1 indica la posición local de la izquierda del robot
initial_orientation = [1,0,0,0]

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
def render():#Para ahorrar lineas, y usando un decorador, renderizar luego de cada acción
    ret, map = gui_algorithm_3.draw_map(maze_format,screen_size,block_size,
        corner_text=(str('text')+' giros'),corner_text_size=font_size
            )
    map = gui_algorithm_3.draw_cube(map,*robot.current_coord,robot._local,cube_margin,
        block_size)
    #Terimna programa#
    cv2.imshow('1',map)
    k = cv2.waitKey(delay)
    if(k == ord('q')):
        return(True)
    return(False)

robot = Robot(initial_orientation,[12,8])
loop = True

if(visualizar):
    def render_dec(func):
        def wraper(*args):
            global loop
            func(*args)
            render()
            k = cv2.waitKey(delay)
            if(k == ord('q')):
                loop = False
        return wraper
    #Para que luego de cada movimiento renderize un cuadro
    robot.avanzar = render_dec(robot.avanzar)
    robot.gira_derecha = render_dec(robot.gira_derecha)
    robot.gira_derecha = render_dec(robot.gira_izquierda)

if(__name__=='__main__'):
    while(loop):
        #Si llegas
        if(maze_format[robot.current_coord[0],robot.current_coord[1]] == -1):
            loop = False
        registro_de_acciones = []
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
        robot.avanzar(maze_format)
        percepcion=robot.see_laterals(maze_format)
        #percepcion es un lista de 4 elementos [izquierda,adelante,derecha,atras]
        #Detectar cruces

        if (percepcion[0] == 0) or (percepcion[2] == 0):
            dir = None
            while(True):
                if((percepcion[0] == 0)and randint(0,1)):
                    #Girará a la izquierda
                    print('L')
                    dir = True ; robot.gira_izquierda();break
                if((percepcion[2] == 0)and randint(0,1)):
                    #Girará a la derecha
                    print('R')
                    dir = False ; robot.gira_derecha();break
        registro_de_acciones.append([robot.current_coord,dir])
        ####################################################################
        ####################################################################
    k = cv2.waitKey(0)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        print('Acciones: {}'.format(action_register),'---------------------------')
    pass
