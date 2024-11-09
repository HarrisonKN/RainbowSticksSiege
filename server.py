import socket
from _thread import *
import sys


server = "192.168.0.169"
port = 5555 #could be a different number

useSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    useSocket.bind((server,port))
except socket.error as e:
    str(e)

useSocket.listen(5)
print("waiting for connection, Server Started")


def threaded_client(connection):
    reply = ""
    while True:
        try:
            data = connection.recieve(2048)
            reply = data.decode("utf-8")

            if not data:
                print("No Data, Client Disconnected")
                break
            else:
                print("Data Received: ", reply)
                print("Sending: ". reply)
            
            connection.sendall(str.encode(reply))
        except:
            break

while True:
    connection,address = useSocket.accept()
    print("Connected to: ",address)

    start_new_thread(threaded_client,(connection))