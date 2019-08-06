class Mapping_tools:
    def __init__(self):
        pass
    def chain_cutter(self,chain):
        """
        Elimina ciclos de uno en uno, por que cuando lo intenté adapter a más ciclos
        se rompío y ya eran muy altas horas de la noche como para andar con esas cosas
        ,si retorna False es por que ya no hay más ciclos, siempre irá a cortar el
        ciclo más largo.Retorna la cadena recortada y el boleano que confirma.
        Takes a hole chain of actions and cut repited parts, to optimizate the actions"""
        #A list with lists, the [element, index1,index2]
        elements = {}
        #Cuenta elementos
        #Cuenta cada cantidad de elemento el la lista
        for (ix,elx)in enumerate(chain):
            if(not (elx in elements)):
                elements[elx] = 0
            elements[elx] += 1
        rep = []
        for e in elements:
            if(elements[e]>1):
                res = [e,[]]
                for (ix,c) in enumerate(chain):
                    if(c == e):
                        res[1].append(ix)
                rep.append(res)
        if(len(rep)>0):
            #Tenemos una lista de cada elemento repetido y sus indices
            #Buscamos el ciclo más grande,
            dif = []
            for r in rep:
                dif.append([ r[0],r[1][-1]-r[1][0] ])
            #Elige el mayor número
            dif.sort(reverse = True ,key=lambda x : x[1])
            max_dif_index = len(chain)+1
            for l in rep:
                if(l[0]==dif[0][0]):
                    max_dif_index = l
            #Remueve
            del chain[max_dif_index[1][0]:max_dif_index[1][-1]]
            return True,chain
        return False,chain

if(__name__=='__main__'):
    M = Mapping_tools()
    #c = [22,1,(21,1),3,(21,1),1,2,3,1,22,5,6,7,(1,56)]
    c = [1,22,2,3,22,5,'a','b',5,'c']
    print(c)
    while(True):
        ret,c = M.chain_cutter(c)
        if (not(ret)):
            break
    print(c)
    pass
