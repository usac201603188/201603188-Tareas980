import socket
import binascii
import os

SERVER_ADDR="localhost"
SERVER_PORT=9800
BUFFER_SIZE= 64 * 1024

server_sock=socket.socket()
server_sock.bind((SERVER_ADDR,SERVER_PORT))
server_sock.listen(100)

while True:
    print("\nEsperando conexion remota...")
    conn, addr = server_sock.accept()
    try:
        print("\nConexion establecida desde ", addr)
        while True:
            data=conn.recv(BUFFER_SIZE)
            if(data==binascii.unhexlify("01")):
                conn.sendall(binascii.unhexlify("CC")) 
                data=conn.recv(BUFFER_SIZE)
                conn.sendall(binascii.unhexlify("CC"))
                audio= "arecord -d " +str(int(data)) +" -f U8 -r 8000 201603188_server.wav"
                os.system(audio)
                conn.sendall(binascii.unhexlify("CC"))
                data=0

            elif(data==binascii.unhexlify("02")):
                archivo = open("201603188_server.wav","rb")
                conn.sendall(archivo)
                data=0
            elif(data==binascii.unhexlify("03")):
                #print("se recibio: ",data)
                conn.sendall(binascii.unhexlify("CC"))
                break
            
    except KeyboardInterrupt:
        server_sock.close()
    finally:
        server_sock.close()
