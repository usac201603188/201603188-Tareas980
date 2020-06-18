import socket
import binascii
import os

SERVER_ADDR="localhost"
SERVER_PORT=9800
BUFFER_SIZE= 64 * 1024

sock=socket.socket()
sock.connect((SERVER_ADDR,SERVER_PORT))


while True:
    try:
        message=input("Comando que quiere enviar: ")        #DRRP se hace un ciclo en el que se preguntara que quiere hacer el usuario
        sock.sendall(binascii.unhexlify(message))           #DRRP guardo el dato en message para usarlo mas tarde
        data=sock.recv(BUFFER_SIZE)
        if(data==binascii.unhexlify("CC")):                 
            print("Se ha confirmado la solicitud")

        if(message=="01"):                              #DRRP toda esta seccion se usa para indicar que grabe y luego cuantos segundos
            duracion=input("ingrese la duracion de la grabacion: ") 
            sock.sendall(duracion.encode())
            if(data==binascii.unhexlify("CC")):
                print("Se ha comenzado la grabacion")
                if(data==binascii.unhexlify("CC")):
                    print("Se ha finalizado la grabacion")

        elif message=="02":                                 #DRRP se le indica que se desea transferir el archivo
            print("Se transferira el archivo")
            data=sock.recv(BUFFER_SIZE)
            audio_nuevo=open("201603188_client.wav","wb")
            while data:
                data=sock.recv(BUFFER_SIZE)
                audio_nuevo.write(data)
            audio_nuevo.close()
            print("Transferencia exitosa \nReproduccion de audio")
            os.system("aplay 201603188_client.wav")

        elif message=="03":                         #DRRP por ultimo se desconecta
            sock.close()




        


    finally:
        sock.close()