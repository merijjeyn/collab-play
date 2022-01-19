
from _thread import *
import socket
import json


PORT = 8080               
SERVER_IP = '137.117.158.139'


class SingletonMeta(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Network(metaclass=SingletonMeta):
    def __init__(self, gameName, username=''):
        self.gameName = gameName
        self.username = username

    def start_host_connection(self, player_action):
        self.player_action = player_action
        start_new_thread(self.host_connection, ())

    def host_connection(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((SERVER_IP, PORT)) 
        message = {'type': 'create_game', 'gamename': self.gameName}
        sock.send(json.dumps(message).encode('utf-8'))

        while True:
            data = json.loads(sock.recv(1024).decode())
            print('Received message: ', data)

            if data['type'] == 'join_game':
                self.player_action(data['username'], data['type'])
            else:
                self.player_action(data['username'], data['type'], data['key'])


    def start_player_connection(self):
        if not self.username:
            raise Exception("Username not initialized for player")
        
        self.player_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if MULTIPLE_CLIENTS_ON_SAME_MACHINE:
            print('Local port?')
            localPort = input()
            self.player_socket.bind(('0.0.0.0', int(localPort)))
        
        self.player_socket.connect((SERVER_IP, PORT))
        message = {'type': 'join_game', 'gamename': self.gameName, 'username': self.username}
        self.player_socket.send(json.dumps(message).encode('utf-8'))


    def make_action(self, type, key):
        if not self.username:
            raise Exception("Username not initialized for player")
        
        message = {'type': type, 'key': key, 'username': self.username}
        print("Sending message: ", message)
        self.player_socket.send(json.dumps(message).encode('utf-8'))

    def __del__(self):
        # destroy the player socket
        if self.player_socket:
            self.player_socket.close()