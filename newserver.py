import socket 
a=socket.socket()
va='127.0.0.1'
host=8712
a.bind((va,host))
print 'binded'
a.listen(5)
print 'listening'
i,address=a.accept()
print i.recv(1024)
i.send('helloworld')
i.close()
