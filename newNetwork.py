import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.169"
        self.port = 5555
        self.address = (self.server ,self.port)
        self.position = self.connect()
        
    def getPos(self):
        return self.position
    
    def connect(self):
        try:
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(2048)) #when we connect, send information immediately
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)