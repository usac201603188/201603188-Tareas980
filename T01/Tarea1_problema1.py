#Diego Roberto Roche Palacios 201603188
#Proyectos980

"""
Encontrar los primeros N numeros perfectos
Como sugerencia, puede implementar una funcion que encuentre
los divisores propios de un numero, y devuelva una lista con estos
N es un numero que ingresa el usuario
http://es.wikipedia.org/wiki/N%C3%BAmero_perfecto
"""

N = input("ingrese el valor de N: ")
m=0
n=2
lista=[]
ans=0
a=int
while(m<int(N)):
    a=(2**(n-1))*((2**(n))-1)
    for i in range(1,a,1):
        if(a%i==0):
            lista.extend([i])
    for j in lista:
        ans+=j
    if(ans==a):
        m+=1
        print(ans)
    else:
        a=0
        lista=[]
        ans=0
        n+=1


