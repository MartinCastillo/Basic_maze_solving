#|This is the code which you executate
#Aclaración: El giro será intercalado en un lado y otro y las iteraciones son
#los giros individuales de 90 grados
#_________________________________________________________________________________
#|En este código la idea es implemenar un algoritmo que se comporte como lo haría|
#|(Aunque sea mas complicado, los algoritmos anteriores también pueden ser impl_ |
#|ementados en un robor)un robot muy básico, puede obtener la misma información  |
#|que antes, solo que ahora el robot avanzará hasta toparse con una pared, si eso|
#|sucede gira a la izquierda o al la derecha, para hacer esto debemos definir lo |
#|que será un adelante atras derecha e izquierda locales:                        |
#|1 es Arriba, 2 es derecha, 3 es abajo , 4 izquierda                            |
#|Será en una lista de 4 elementos del formato de ciclo:                         |
#|[arriba , derecha , abajo , izquierda]                                         |
#| Ej: si adelante esá a la derecha                                              |
#| (arriba , derecha , abajo , izquierda)                                        |
#| [  4    ,     1     ,   2     ,   3  ]                                        |
#|Por que al mirar a la izquierda el abajo esta a la izquierda, derecha arriba   |
#|etc, en otras palabras, lo de arriba indica el espacio global y la lista es los|
#|lados del cubo.                                                                |
#_________________________________________________________________________________
#Global imports
import numpy as np
from matplotlib import pyplot as plt
import cv2
from time import sleep
from random import randint
#Local imports
import gui_algorithm_2

#Global variables
screen_size = 500
block_size = 25
cube_margin = 5
delay=100
current_coord=[12,8] #Coordenadas de inicio
font_size=2
#Si esta variable es true cambiara de dirección cada cierta cantidad de numeros
#dada por max_iter
turning_direction = True #Esto es derecha, si es False es izquierda
fliping = False
max_iter = 4
random_fliping = False #Giros aleatorios,para que funcione debes desactivar fliping
#La permutación antes descrita, cambiala si quieres variar la dirección inicial
#         arriba derecha   abajo  izquierda
_local =  [   1 ,   2     ,   3      ,4]
#Si gira a la derecha _local = [4,1,2,3]
#2 * derecha = abajo ,_local = [3,4,1,2s]
#a la izquierda _local = [2,3,4,1] = 3 * derecha
#Llamaremos esta rotación a la drecha r

#nxn matrix for the maze format, 0 is nothing in the place, 999 is wall,-1 is ending
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
action_register=[0]
#see_laterals function

def r(local_list):
    """
    Una permutación el ciclo dado local_list Debe tener un largo 4"""
    res = []
    res.append(local_list[3]);res.append(local_list[0])
    res.append(local_list[1]);res.append(local_list[2])
    return(res)

def avanzar(ycoord,xcoord,local_list):
    """
    Esta función avanza una celda en la direccón que la lista del ciclo
    indique, luego retorna las nuevas cooordenadas.
    """
    #Dirección
    dir = local_list.index(1)
    #si es 0 apunta arriba,si es 1 es a la derecha,si es 2 abajo y 3 izquierda
    new_ycoord=ycoord;new_xcoord=xcoord
    if(dir==0):
        new_ycoord = ycoord-1
    elif(dir==1):
        new_xcoord = xcoord+1
    elif(dir==2):
        new_ycoord = ycoord+1
    elif(dir==3):
        new_xcoord = xcoord-1
    else:
        print('Error en función "avanzar"')
    return(new_ycoord,new_xcoord)

def _consultar_YoX(num1,num2,ycoord,xcoord):
    """Consulta el eje Y o X dependiendo de la entrada, si num1=-1 consulta arriba
    ,si num1=1 lo hace abajo , si num2=-1 derecha, num2=1 es izquierda,considere
    que si consulta en un eje el otro num deve valer 0"""
    return(True if(maze_format[ycoord+num1,xcoord+num2] !=999) else False)

def disponible(maze_format,ycoord,xcoord,local_list):
    """Esta función consulta si la en la direccón indicada,coordenadas y en el mapa
    hay una interferencia"""
    dir = local_list.index(1)
    #si es 0 apunta arriba,si es 1 es a la derecha,si es 2 abajo y 3 izquierda
    if(dir==0):
        return(_consultar_YoX(-1,0,ycoord,xcoord))
    elif(dir==1):
        return(_consultar_YoX(0,1,ycoord,xcoord))
    elif(dir==2):
        return(_consultar_YoX(1,0,ycoord,xcoord))
    elif(dir==3):
        return(_consultar_YoX(0,-1,ycoord,xcoord))
    else:
        print('Error en función "disponible"')

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
    iters=0
    while(True):
            if(maze_format[current_coord[0],current_coord[1]] == -1):
                break
            ret, map = gui_adaptada.draw_map(maze_format,screen_size,block_size,
                corner_text=str(iters),corner_text_size=font_size,corner_text_color=(100,100,255)
                    )
            map = gui_adaptada.draw_cube(map,current_coord[0],current_coord[1],
                _local,cube_margin,block_size
                    )
            cv2.imshow('1',map)
            k = cv2.waitKey(delay)
            if(k==ord('q')):
                break
            #print('iters+=1')
            #Analizar alrededores
            res_matrix=see_laterals(maze_format,current_coord[0],
                current_coord[1]
                    )
            #Si en la direccón de _local no hay nada avanza
            if(disponible(maze_format,current_coord[0],current_coord[1],_local)):
                current_coord=avanzar(current_coord[0],current_coord[1],_local)
                #Esta condición es para no incluir innecesarios 'Avanza'
                if(action_register[::-1][0]!='Avanza'):
                    action_register.append('Avanza')
            #Si no, gira dependiendo de la variable global turning_direction
            else:
                iters+=1
                if(turning_direction):
                    _local=r(_local)
                    action_register.append('Gira derecha')
                else:
                    _local=r(r(r(_local)))
                    action_register.append('Gira izquierda')
                if(iters%max_iter==0)and(fliping):
                    turning_direction = not(turning_direction)
                    action_register.append('cambio turning_direction a {}'.format(
                        turning_direction
                            ))
                #Cambia de dirección de forma aleatoria(Funcionaba muy mal)
                if(random_fliping):
                    turning_direction = [True,False][randint(0,1)]
                    action_register.append('cambio turning_direction a {}'.format(
                        turning_direction
                            ))
    ret, map = gui_adaptada.draw_map(maze_format,screen_size,block_size,
        corner_text=(str(iters)+' giros'),corner_text_size=font_size
            )
    map = gui_adaptada.draw_cube(map,current_coord[0],current_coord[1],
        _local,cube_margin,block_size
            )
    cv2.imshow('1',map)
    k = cv2.waitKey(0)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        print('Iterations: {}'.format(iters),'---------------------------')
        print('Acciones: {}'.format(action_register),'---------------------------')
    pass
