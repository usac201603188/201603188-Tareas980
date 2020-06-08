#Diego Roberto Roche Palacios 201603188
#Proyectos980

"""
Problema 2
----------
Encontrar los primeros N numeros amigos.
Debe preguntar al usuario el valor de N antes de iniciar.
http://es.wikipedia.org/wiki/N%C3%BAmeros_amigos
"""

######## Variables ########

N = input("Ingrese el valor de numeros amigos a calcular: ") #Se solicitan los numeros amigos <=4

m=0
a=2
b=int #no es necesario pero si no me pierdo
lista1=[]
lista2=[]
ans1=0
ans2=0

while (m<int(N)):
    for i in range(1,a,1):
        if(a%i==0):             #Itero los dividendos de mi numero
            lista1.extend([i])
    for j in lista1:
        ans1+=j                 #Sumo los dividendos para el posible numero amigo
    for k in range(1,ans1,1):
        if(ans1%k==0):
            lista2.extend([k])  #itero los dividendos del posible numero amigo
    for l in lista2:
        ans2+=l                 #sumo los dividendos
    if(ans2==a):
        if(ans1!=a):            #Compruebo si son amigos y desecho los numeros perfectos
            print("Los números amigos son:", str(a)," y ", str(ans1))
            m+=1
            a=ans1              #Este es para que no se repita el numero amigo
    else:
        #print(a)
        a+=1
        lista1=[]
        lista2=[]
        ans1=0
        ans2=0    

