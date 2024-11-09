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

useSocket.listen()
print("waiting for connection, Server Started")


position = [(0,0),(100,100)] #player1 , player2

def read_position(str):
    str = str.split(",")
    return int(str[0]),int(str[1])

def send_position(tup):
    return str(tup[0]) + "," +str(tup[1])

def threaded_client(connection, currentPlayer):
    connection.send(str.encode(send_position(position[currentPlayer])))
    reply = ""
    while True:
        try:
            data = read_position(connection.recv(2048).decode())
            position[currentPlayer] = data

            if not data:
                print("No Data, Client Disconnected")
                break
            else:
                if currentPlayer == 1:
                    reply = position[0]
                else:
                    reply = position[1]
                print("Data Received: ", data)
                print("Data Sending: ", reply)
            
            connection.sendall(str.encode(send_position(reply)))
        except:
            break
    
    print("Lost Connection")
    connection.close()

currentPlayer = 0

while True:
    connection,address = useSocket.accept()
    print("Connected to: ",address)

    start_new_thread(threaded_client,(connection, currentPlayer))
    currentPlayer += 1