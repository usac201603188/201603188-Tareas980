#Diego Roberto Roche Palacios 201603188
#Proyectos980

"""
Problema 2
----------
Encontrar los primeros N numeros amigos.
Debe preguntar al usuario el valor de N antes de iniciar.
http://es.wikipedia.org/wiki/N%C3%BAmeros_amigos
"""


def multiplos(numerito):
    lista=[]
    for i in range(1,numerito,1):
        if(numerito%i==0):             #Itero los dividendos de mi numero
            lista.extend([i])
    return(lista)

def suma(lista):
    respuesta=0
    for j in lista:
        respuesta+=j                 #Sumo los dividendos para el posible numero amigo
    return(respuesta)


######## Variables ########

N = input("Ingrese el valor de numeros amigos a calcular: ") #Se solicitan los numeros amigos 

m=0
a=2
while (m<int(N)):
    lista1=multiplos(a)
    ans1=suma(lista1)
    lista2=multiplos(ans1)
    ans2=suma(lista2)
    #print(lista1,ans1,lista2,ans2)
    if(ans2==a):
        if(ans1!=a):            #Compruebo si son amigos y desecho los numeros perfectos
            print("Los números amigos son:", str(a)," y ", str(ans1))
            m+=1
            a=ans1+1              #Este es para que no se repita el numero amigo
        else:
            a+=1
    else:
        #print(a)
        a+=1
        

