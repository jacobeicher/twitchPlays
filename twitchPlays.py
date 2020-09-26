import win32api
import win32con
import time
import socket
import put



server = "irc.twitch.tv"
port = 6667
nickname = 'testBot'
token = "oauth:"
channel = "#ddibwynt"


up = 0x57 # w
left = 0x41 # a
down = 0x53 # s
right = 0x44 # d
a = 0x5A # z 
b = 0x58 # x
select = 0x43 # c
start = 0x56 # v
lShoulder = 0x46 # f
rShoulder = 0x47 # g

validKeys = ['up', 'left', 'right', 'down', 'a', 'b', 'start', 'select', 'lShoulder', 'rShoulder']

mappedResponses = {
    'up': 0x57,
    'left': 0x41,
    'down': 0x53,
    'right': 0x44,
    'a': 0x5A,
    'b': 0x58,
    'select': 0x43,
    'start': 0x56,
    'lShoulder': 0x46,
    'Rshoulder': 0x47
}

sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\r\n".encode('utf-8'))
sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
sock.send(f"JOIN {channel}\r\n".encode('utf-8'))

try:
    while True:
        resp = sock.recv(2048).decode('utf-8')
        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))
        elif len(resp) > 0:
            newResp = resp.split(":")
            command =  str(newResp[2].strip(" \r\n").lower())
            print(newResp[2])
            if(command in validKeys):
                input = mappedResponses[str(command)]
                print('input: ', input)
                win32api.keybd_event(input, 0, 0, 0)
                time.sleep(.1)
                win32api.keybd_event(input, 0, win32con.KEYEVENTF_KEYUP, 0)
            else:
                print('invalid input: ', command)
        time.sleep(.1)
                


except KeyboardInterrupt:
    sock.close()
    exit()


