import socket
import pickle
from _thread import *
from player import Player
from character import Character


server = "192.168.0.169"
port = 5555 #could be a different number

useSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    useSocket.bind((server,port))
except socket.error as e:
    str(e)

useSocket.listen()
print("waiting for connection, Server Started")

players = [Player(0,0,50,50,(255,0,0)), Player(100,100, 50,50,(0,255,0)), Character(100, 100, 'RainbowSticksSiege/Images/Characters/Fighter/Idle.png', speed=5, rows=2, columns=4) ]

def threaded_client(connection, currentPlayer):
    connection.send(pickle.dumps(players[currentPlayer]))
    reply = ""
    while True:
        try:
            data = pickle.loads(connection.recv(2048))
            players[currentPlayer] = data

            if not data:
                print("No Data, Client Disconnected")
                break
            else:
                reply = players[1 - currentPlayer]
                print("Data Received: ", data)
                print("Data Sending: ", reply)
            
            connection.sendall(pickle.dumps(reply))
        except:
            break
    
    print("Lost Connection")
    connection.close()

currentPlayer = 0

while True:
    connection,address = useSocket.accept()
    print("Connected to: ",address)

    start_new_thread(threaded_client, (connection, currentPlayer))
    currentPlayer += 1