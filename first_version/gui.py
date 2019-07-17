#All the functions needed to show graphically the info
#Este archivo sera usado por todas las versiones de prueba de los algoritmos
import cv2; import numpy as np

def draw_cube(map,ycoord,xcoord,margin=15,cube_size=50,color=(100,100,255)):
    yres = ycoord*cube_size; xres = xcoord*cube_size
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
    map[yres+margin:yres+(cube_size-margin),
        xres+margin:xres+(cube_size-margin)]=color
    return(map)

def draw_map(maze_format,screen_size=500,block_size=50,wall_color=255,end_color
    =(100,255,100) , passed_color = (50), corner_text=' ',corner_text_size=2,
        corner_text_color=(0,0,200)
        ):
    """
    It recives a screen size, block size,wall color,Ending block color and nxn
    matrix where:
    -0 is nothing
    -1 is wall
    -2 is ending
    -3 passed
    """
    temp_map=np.zeros((screen_size,screen_size),np.uint8)
    map=cv2.cvtColor(temp_map,cv2.COLOR_GRAY2BGR)

    for i in range(screen_size):
        for j in range(screen_size):
            if((i%block_size == 0)and(j%block_size == 0)):
                block_number = maze_format[i//block_size,j//block_size]
                if(block_number==1):
                    map[i:i+block_size,j:j+block_size]=wall_color
                #Ending block
                if(block_number==2):
                    map[i:i+block_size,j:j+block_size]=end_color
                if(block_number==3):
                    map[i:i+block_size,j:j+block_size]=passed_color

                #map[i,j]=(255,0,0) #Dwars a point grid
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(map,corner_text,(0,screen_size-block_size//2),font,corner_text_size
        ,corner_text_color,1,cv2.LINE_AA
            )
    return(map)

if(__name__=='__main__'):
    pass
