import socket
import binascii
import os

SERVER_ADDR="localhost"                     #DRRP se usará en la misma maquina
SERVER_PORT=9800
BUFFER_SIZE= 64 * 1024

server_sock=socket.socket()
server_sock.bind((SERVER_ADDR,SERVER_PORT))
server_sock.listen(100)                     #DRRP 1 activo y 99 en cola

while True:
    print("\nEsperando conexion remota...")
    conn, addr = server_sock.accept()       #DRRP realiza la conección a un cliente
    try:
        print("\nConexion establecida desde ", addr)
        while True:
            data=conn.recv(BUFFER_SIZE)         #DRRP recepcion de datos
            if(data==binascii.unhexlify("01")):         #DRRP este metodo hara la grabacion, enviando tres veces el ack
                conn.sendall(binascii.unhexlify("CC")) 
                data=conn.recv(BUFFER_SIZE)
                conn.sendall(binascii.unhexlify("CC"))
                audio= "arecord -d " +str(int(data)) +" -f U8 -r 8000 201603188_server.wav"
                os.system(audio)
                conn.sendall(binascii.unhexlify("CC"))  #DRRP  hay un pequeño bug en esta linea que no se solucionar
                data=0

            elif(data==binascii.unhexlify("02")):           #DRRP en esta parte se hara el envio del archivo
                archivo = open("201603188_server.wav","rb")
                conn.sendall(archivo)
                data=0
            elif(data==binascii.unhexlify("03")):           #DRRP se desconecta del cliente
                #print("se recibio: ",data)
                conn.sendall(binascii.unhexlify("CC"))
                break

    except KeyboardInterrupt:
        server_sock.close()
    finally:
        server_sock.close()
