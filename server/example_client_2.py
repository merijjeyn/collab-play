import socket
import json


PORT = 8080               
SERVER_IP = '137.117.158.139'
GAMENAME = 'TEST1'

print('Port?')
port = int(input())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', port))
sock.connect((SERVER_IP, PORT))

print('Action?')
action = input()

if action == 'create':
    message = {'type': 'create_game', 'gamename': GAMENAME}
    sock.send(json.dumps(message).encode('utf-8'))
    while True:
        request_string = json.loads(sock.recv(1024).decode())
        print('Received message from one of the clients', request_string)

elif action == 'join':
    print("Username?")
    username = input()
    message = {'type': 'join_game', 'username': username, 'gamename': GAMENAME}
    sock.send(json.dumps(message).encode('utf-8'))
    
    while True:
        inp = input()
        message = {'type': 'keydown', 'username': username, 'key': inp}
        print('Sent ' + str(message))
        sock.send(json.dumps(message).encode('utf-8'))
