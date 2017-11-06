import socket
HOST = '10.25.1.58'
#HOST = socket.gethostbyname('localhost')
#PORT = 2000
PORT = 2009
tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcp_client_socket.connect((HOST,PORT))
message = "Ana Giseli Almeida"
byte_msg = message.encode('utf-8')
tcp_client_socket.send(byte_msg)
data = tcp_client_socket.recv(1024)
tcp_client_socket.close
print("MSG recebida: ", repr(data))



# 10.25.3.174
