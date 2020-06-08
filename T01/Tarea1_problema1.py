#Diego Roberto Roche Palacios 201603188
#Proyectos980

"""
Encontrar los primeros N numeros perfectos
Como sugerencia, puede implementar una funcion que encuentre
los divisores propios de un numero, y devuelva una lista con estos
N es un numero que ingresa el usuario
http://es.wikipedia.org/wiki/N%C3%BAmero_perfecto
"""

##########     Metodos      ##############

def recorrido(N):
    m=0
    lista=[]
    ans=0
    a=1
    while(m<int(N)):                
        for i in range(1,a,1):
            if(a%i==0):
                lista.extend([i])          #Realiza una lista con todos los multiplos
        for j in lista:
            ans+=j                         #Suma cada multiplo
        if(ans==a):
            m+=1
            print(ans)                     #va mostrando cada número perfecto
        else:
            a+=1                            #Este es comentario para mi: no se si es 
            lista=[]                       #necesario para que resetee el while
            ans=0
         


##########    Variables       ############
N = input("ingrese el valor de N: ")   #Aqui solicita cuantos numero perfectos se desean
recorrido(N)

"""
##########    Variables       ############
N = input("ingrese el valor de N: ")   #Aqui solicita cuantos numero perfectos se desean
m=0
n=2
lista=[]
ans=0
a=int

while(m<int(N)):                
    a=(2**(n-1))*((2**(n))-1)          #Formula 1:  Encontrada en la documentación
    for i in range(1,a,1):
        if(a%i==0):
            lista.extend([i])          #Realiza una lista con todos los multiplos
    for j in lista:
        ans+=j                         #Suma cada multiplo
    if(ans==a):
        m+=1
        print(ans)                     #va mostrando cada número perfecto
    else:
        a=0                            #Este es comentario para mi: no se si es 
        lista=[]                       #necesario para que resetee el while
        ans=0
        n+=1
"""

#Posible optimizacion, calcular los numeros primos y trabajar con esos en la formula 1
#Recomendacion, el N mientras mas grande, mas tardado el procesamiento. 
