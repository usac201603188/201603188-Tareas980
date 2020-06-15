#Diego Roberto Roche Palacios 201603188
#Proyectos 980

class matriz(object):

    def __init__(self,data=[]):     #metodo constructor
        self.data=list(data)

    def dimensions(self):          #Este metodo indica las dimensiones de la matriz; regresa una lista
        try:
            len(self.data[0])
        except TypeError:
            return [1,len(self.data)]
        return[len(self.data),len(self.data[0])]

    def equalLenghts (self, secondmatrix):      #Indicador de igualdad de dimensiones
        return self.dimensions() == secondmatrix.dimensions()

    def __add__(self, sumando):             #Sobrecarga del operador suma, aplicado a matrices
        if self.equalLenghts(sumando):
            result=[]
            for i in range(self.dimensions()[0]):
                fila=[]
                for j in range(self.dimensions()[1]):
                    fila.append(self.data[i][j]+sumando.data[i][j])
                result.append(fila)
            return matriz(result)
        else:
            raise ErrorDimensional(self.dimensions(), sumando.dimensions())

    def __sub__(self, sustraendo):
        if self.equalLenghts(sustraendo):
            result=[]
            for i in range(self.dimensions()[0]):
                fila=[]
                for j in range(self.dimensions()[1]):
                    fila.append(self.data[i][j]-sustraendo.data[i][j])
                result.append(fila)
            return matriz(result)
        else:
            raise ErrorDimensional(self.dimensions(), sustraendo.dimensions())

    def multiHelper(self, ayudaPLS):
        newList=[]
        for i in range(ayudaPLS):
            newList.append(0)
        return newList

    def __mul__(self, multiplicador):
        if type(multiplicador)==int or type(multiplicador)==float:
            result=[]
            for i in range(self.dimensions()[0]):
                fila=[]
                for j in range(self.dimensions()[1]):
                    fila.append(self.data[i][j]*multiplicador)
                result.append(fila)
            return matriz(result)
        elif type(multiplicador)==list or type(multiplicador)==matriz:
            if (self.dimensions()[1]==multiplicador.dimensions()[0]):
                result=[]
                for i in range(self.dimensions()[0]):
                    fila=[]
                    helper=self.multiHelper(self.dimensions()[0])
                    for j in range(self.dimensions()[1]):
                        multi=[]
                        for k in range(multiplicador.dimensions()[1]):
                            multi.append(a[i][j]*b[j][k])
                        fila.append(helper=helper+multi)
                    result.append(fila)
                return matriz(result)

            else:
                raise ErrorDimensional(self.dimensions(), multiplicador.dimensions())
        else:
            raise TypeError("Ingresar campos validos a mutliplicar")


    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return self.__str__()


class ErrorDimensional(Exception): #Se levanta esta excepcion cuando la longitud de dos vectores a sumar/restar
    def __init__(self,m1,m2):       #no son iguales. Se reciben como parametros las longitudes de ambos vectores
        self.m1=m1
        self.m2=m2

    def __str__(self):
        return str("Para esta opeacion se requiere que, "+str(self.m1)+" y "+str(self.m2)+" cumplan con dimensiones especificas.")

    def __repr__(self):
        return self.__str__()









a=matriz([[1,2],[3,4]])
b=matriz([[5,6],[7,8]])
c=matriz([[99,1],[88,2],[77,3]])
d=matriz([[1],[2],[3]])
e=matriz([[1,7],[0,2]])
f=matriz([1,2,3,5])
g=matriz([5])
print("prueba2")

 