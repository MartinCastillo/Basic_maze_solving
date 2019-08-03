
#Por ahora no se realizará una gui importante
#All the functions needed to show graphically the info
#Este archivo sera usado por todas las versiones de prueba de los algoritmos
import cv2; import numpy as np

def draw_cube(map,ycoord,xcoord,margin=5,block_size=20,color=(100,100,255)):
    yres = ycoord*block_size; xres = xcoord*block_size
    """
    This function graph a cube in the x,y coords over the map,
    the format for x,y coords are the index in the maze_format
    matrix, for the graph in a 500x500 we multply x,y by 50 or cubesize
    |Parameters:
    -map = map image
    -xcoord = x coordinate for the cube
    -ycoord = y coordinate for the cube
    -margin = cube margin to the walls, DEFAULT = 15
    -cube_size = cube size, DEFAULT = 50
    -color = cube color DEFAULT = (50,50,255) (soft red)
    """
    map[yres+margin:yres+(block_size-margin),
        xres+margin:xres+(block_size-margin)]=color
    return(map)

def draw_map(maze_format,screen_size=500,block_size=25,wall_color=30,end_color
    =(100,255,100) , passed_color = (50), corner_text=' ',corner_text_size=2,
        corner_text_color=(0,0,200)
            ):
    """
    It recives a screen size, block size,wall color,Ending block color , nxn
    matrix where:
    -0 is nothing
    -999 is wall
    --1 is ending
    -other passed x times
    passed_color , corner_text ,corner_text_size ,corner_text_color
    El block_size debe ser divisor de screen_size
    """
    temp_map=np.zeros((screen_size,screen_size),np.uint8)
    map=cv2.cvtColor(temp_map,cv2.COLOR_GRAY2BGR)
    if(not(screen_size%block_size==0)):
        print('''El tamaño de la pantalla y el de los bloques no son compatibles
            ,for favor revise las especificaciones de la función draw_map'''
                )
        return(False,map)

    for i in range(screen_size):
        for j in range(screen_size):
            if((i%block_size == 0)and(j%block_size == 0)):
                #print([i//block_size,j//block_size])
                block_number = maze_format[i//block_size,j//block_size]
                if(block_number==999):
                    map[i:i+block_size,j:j+block_size]=wall_color
                #Ending block
                elif(block_number==-1):
                    map[i:i+block_size,j:j+block_size]=end_color
                else:
                    if(block_number<=4):
                        map[i:i+block_size,j:j+block_size]=(255-block_number*passed_color)
                    else:
                        map[i:i+block_size,j:j+block_size]=passed_color
                #map[i,j]=(255,0,0) #Dwars a point grid
    font = cv2.FONT_HERSHEY_SIMPLEX
    """
    Fonts
    FONT_HERSHEY_COMPLEX, FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL,
    FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN,FONT_HERSHEY_DUPLEX,
    FONT_HERSHEY_SCRIPT_SIMPLEX, FONT_HERSHEY_SCRIPT_COMPLEX, FONT_ITALIC
    """
    cv2.putText(map,corner_text,(0,screen_size-block_size//2),font,corner_text_size
        ,corner_text_color,1,cv2.LINE_AA
            )
    return(True,map)

if(__name__=='__main__'):
    pass
