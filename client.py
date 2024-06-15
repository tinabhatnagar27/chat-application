# Client
from socket import *
import time

localhost = '127.0.0.1'
port = 91
client = socket(AF_INET,SOCK_STREAM)

# Now We COnnect TO The Server 
try:
    client.connect((localhost,port))
    print(f'Client Is connected to the server at port number{port}')

# Rec Data
    RecData = client.recv(1024).decode()
    print('server:',RecData)



    client.send(bytes('Hello Server'+  time.ctime(),'utf-8'))
    print('Hello Message is send to server')
        
    while True:
        input_user = input("Client:    ")
        client.send(bytes(input_user,'utf-8'))
        
        if input_user.lower() == 'bye':
            print('Bye !🖐 Ending the Chat')
            break
        # Response From Server
        response_from_Server = client.recv(1024).decode()
        print('Server:  ',response_from_Server)
        
except Exception as e:
    print('Error ',e)
finally:
    
    client.close()
    print("Connection Closed")