#!/usr/bin/python3


import socket
import calculadorafunciones


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 1235))
mySocket.listen(5)

try:
	while True:
		print('Waiting for connections')
		(recvSocket, address) = mySocket.accept()
		print('Request received:')

		bytes_received = recvSocket.recv(2048)
		request = str(bytes_received,'utf-8')
		
		print(request);
		resource = request.split()[1]
		print("Recurso: ", resource)
		_, op1, operacion, op2 = resource.split('/')
		print('Answering back...')
		respuesta1 = op1 + " " + operacion + " " + op2 + " = " + 
					str(int(op1)+int(op2))

		num1 = float(op1)
		num2 = float(op2)
		respuesta1 = calculadorafunciones.funciones[operacion](num1,num2)

		recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
						str(op1) + " " + str(operacion) + " " + str(op2) +
						"= " str(respuesta1),
				 		'utf-8'))
		recvSocket.close()
except KeyboardInterrupt:
	print("Closing binded socket")
mySocket.close()
