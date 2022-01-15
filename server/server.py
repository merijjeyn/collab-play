
import socket

import email
from _thread import *
import threading
import pprint
from io import StringIO
import json
def start_server():
    # Define socket host and port
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8080
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print('Listening on port %s ...' % SERVER_PORT)

    while True:    
        # Wait for client connections
        client_connection, client_address = server_socket.accept()
        print('new ', client_connection, client_address)
        start_new_thread(new_connection, (client_connection,))
    # Close socket
    server_socket.close()



socket_lock = threading.Lock() #TODO: lock for each game

def sendfunction(sock, data):
    with socket_lock:
        sock.send(json.dumps(data).encode('utf-8'))



class game:
    def __init__(self, name, socket):
        self.socket = socket
        self.gamename = name
        self.users = set()
#        self.socket_mutex = mutex()


GAMES = {}

def create_game(socket, gamename):
    new_game = game(gamename,socket)
    GAMES[gamename] = new_game
    print('create_game', gamename, socket)


def join_game(client_connection, username, gamename):    
    GAMES[gamename].users.add(username)
    sendfunction(GAMES[gamename].socket, {"type":"join_game", "username":username}) 
    print('join_game: ',username, gamename)
    while True:
        request_string = client_connection.recv(1024).decode()
        print('new key stroke: ', request_string)
        sendfunction(GAMES[gamename].socket, json.loads(request_string))


def new_connection(client_connection):
    request_string = client_connection.recv(1024).decode()

    new_message = json.loads(request_string)
    if new_message['type'] == "create_game":
        create_game(client_connection, new_message['gamename'])
    elif new_message['type'] == "join_game":
        join_game(client_connection, new_message['username'], new_message['gamename'])

start_server()

