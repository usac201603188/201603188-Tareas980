import socket
import binascii

SERVER_ADDR="localhost"
SERVER_PORT=9800
BUFFER_SIZE= 64 * 1024

sock=socket.socket()
sock.connect((SERVER_ADDR,SERVER_PORT))


while True:
    try:
        message=input("Comando que quiere enviar: ")
        sock.sendall(binascii.unhexlify(message))
        data=sock.recv(BUFFER_SIZE)
        if(data==binascii.unhexlify("CC")):
            print("Se ha confirmado la solicitud")

        if(message=="01"):
            duracion=input("ingrese la duracion de la grabacion: ")
            sock.sendall(duracion.encode())
            if(data==binascii.unhexlify("CC")):
                print("Se ha comenzado la grabacion")
                if(data==binascii.unhexlify("CC")):#data seguira siendo CC no cambia antes de este if
                    print("Se ha finalizado la grabacion")

        elif message=="02":
            print("Se transferira el archivo")
            data=sock.recv(BUFFER_SIZE)#Se pierde BUFF_SIZE bytes del archivo
            audio_nuevo=open("201603188_client.wav","wb")
            while data:
                data=sock.recv(BUFFER_SIZE)
                audio_nuevo.write(data)
            audio_nuevo.close()
            print("Transferencia exitosa \nReproduccion de audio")
            os.system("aplay 201603188_client.wav")

        elif message=="03":
            sock.close()




        


    finally:
        sock.close()
