import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 12345
server_socket.bind((host,port))
print("Server socket sucessfully Created on IP : {} at port {} ".format(host,port))
server_socket.listen()
print("Server is waiting for clients to connect .... \n\n")
client_socket,client_addr = server_socket.accept()
print("Client is connected")
print("Client's IP {}:{}\n\n".format(*client_addr))
f = open(input("Enter path to your file "),'rb')
name =f.name
client_socket.send(name.encode())
for line in f:    
    client_socket.send(line)
else :
    client_socket.send("EOF".encode()) 
    client_socket.close()
    server_socket.close()


