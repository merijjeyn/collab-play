

from http import client
from pickle import TRUE
import socket            
import json
from _thread import *
import threading
import keyboard

# Create a socket object
 
# Define the port on which you want to connect
PORT = 8080               
SERVER_IP = '137.117.158.139'
# connect to the server on local computer
 
class game_client:
    def __init__(self, username):
        self.username = username
        self.sock = socket.socket()
        self.sock.connect((SERVER_IP, PORT))
        pass
    
    def create_game(self, gamename):
        message = {'type' : 'create_game',  'gamename' : gamename}
        self.sock.send(json.dumps(message).encode('utf-8'))
        self.listen_game()
        #start_new_thread(self.listen_game, ())  # OPEN THREAD TO LISTEN

    def listen_game(self): # LISTENS IN THREAD
        while True:
            request_string = json.loads(self.sock.recv(1024).decode())
            print('listen_game', request_string)
            # IF TYPE JOIN
            # ELIF TYPE SEND KEYS
    
    def join_game(self, gamename):
        message = {'type' : 'join_game', 'username': self.username,  'gamename' : gamename}
        self.sock.send(json.dumps(message).encode('utf-8'))

    def send_key(self, key):
        message = {'type' : 'key', 'username' : self.username, 'key' : key}
        print('sended' ,message)
        self.sock.send(json.dumps(message).encode('utf-8'))


username = input('username?:')
client = game_client(username)

while True:
    action = input('Action? (create - join):')

    if action == 'create':
        gamename = input('give gamename to create?')
        client.create_game(gamename)
    elif action == 'join':
        gamename = input('give gamename to join?')
        client.join_game(gamename)
        print("KNOW YOU INPUTS WILL BE SEND")
        while (True): # LISTEN KEYS
            if keyboard.read_key() == "w":
                client.send_key('w')
            if keyboard.read_key() == "s":
                client.send_key('s')
            if keyboard.read_key() == "a":
                client.send_key('a')            
            if keyboard.read_key() == "d":
                client.send_key('d')
