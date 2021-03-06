#En proceso


#For more easy code design.This class represent a robot, it only can get the info
#from the envrioment that a robot would get, and return an action, forward, turn,rigth
#turn left, backwards.
#The envrioment can get all the robot's physical information
def r(local_list):
    """
    Una permutación al ciclo dado local_list Debe tener un largo 4"""
    res = []
    res.append(local_list[3]);res.append(local_list[0])
    res.append(local_list[1]);res.append(local_list[2])
    return(res)

class Robot:
    def __init__(self,_local,current_coord):
        #La permutación antes descrita, cambiala si quieres variar la dirección inicial
        #arriba derecha   abajo  izquierda
        self._local = _local
        #Si gira a la derecha _local = [4,1,2,3]
        #2 * derecha = abajo ,_local = [3,4,1,2]
        #a la izquierda _local = [2,3,4,1] = 3 * derecha
        #Llamaremos esta rotación a la drecha r
        self.current_coord = current_coord
        pass

    def _avanzar(self,ycoord,xcoord,local_list):
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
        return([new_ycoord,new_xcoord])

    def see_laterals(self,maze_format):
        """
        This function allow you to know the lateral blocks of the cube, it recives
        the map and coordinates of the block and returns the 8 lateral blocs in a
        [left,forward,rigth,backward] array, it has a bolean value
        """
        (x,y)= self.current_coord
        #Now we need to adjust this to the local view of the robot
        #e.g if the robot direction is the rigth [4,1,2,3], the res array would have
        #to be in the form [backward,left,forward,rigth]
        #and to the left [forward,rigth,backward,left]
        res_matrix = maze_format[y-1:y+2,x-1:x+2]
        res = [res_matrix[1,0],res_matrix[0,1],res_matrix[1,2],res_matrix[2,1]]
        #para reconocer giros en el giro o _local, buscamos la posicion del 'izquierda'
        #en la lista que es un 1
        index_of_local_forward = self._local.index(1)
        #Si index_of_local_forward vale 0 , la orientación es 'arriba ', y la lista
        #no se imuta, por cada desface hacemos un giro para ajustar
        for _ in range(4-index_of_local_forward):#El 4- es para que gire en dirección contraria
            res = r(res)
        return(res)

    def _consultar_YoX(self,num1,num2,ycoord,xcoord,maze_format):
        """Consulta el eje Y o X dependiendo de la entrada, si num1=-1 consulta arriba
        ,si num1=1 lo hace abajo , si num2=-1 derecha, num2=1 es izquierda,considere
        que si consulta en un eje el otro num deve valer 0"""
        return(True if(maze_format[ycoord+num1,xcoord+num2] !=999) else False)

    def disponible(self,maze_format,ycoord,xcoord,local_list):
        """Esta función consulta si la en la direccón indicada,coordenadas y en el mapa
        hay una interferencia"""
        dir = local_list.index(1)
        #si es 0 apunta arriba,si es 1 es a la derecha,si es 2 abajo y 3 izquierda
        if(dir==0):
            return(self._consultar_YoX(-1,0,ycoord,xcoord,maze_format))
        elif(dir==1):
            return(self._consultar_YoX(0,1,ycoord,xcoord,maze_format))
        elif(dir==2):
            return(self._consultar_YoX(1,0,ycoord,xcoord,maze_format))
        elif(dir==3):
            return(self._consultar_YoX(0,-1,ycoord,xcoord,maze_format))
        else:
            print('Error en función "disponible"')

    def avanzar(self,maze_format):
        if(self.disponible(maze_format,self.current_coord[0],self.current_coord[1],self._local)):
            self.current_coord=self._avanzar(self.current_coord[0],self.current_coord[1],self._local)
            #print('avanza')
        else:
            print('Una pared se interpone, obj:{} chocando con ella'.format(self.__class__.__name__))
            pass

    def gira_derecha(self):
        self._local=r(self._local)
        #print('gira a la derecha')

    def gira_izquierda(self):
        self._local=r(r(r(self._local)))
        #print('gira a la izquierda')
