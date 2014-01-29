import socket
a=socket.socket()
va='127.0.0.1'
host=8712
a.connect((va,host))
print 'connect'
a.send('Hello')
print a.recv(1024)
a.close()
