#import socket module
from socket import * #from the socket library, import everything

serverSocket = socket(AF_INET, SOCK_STREAM) #defining a new socket
#Prepare a sever socket
serverPort = 1234 #assigning the port number with 1234
serverSocket.bind(("",serverPort)) # Bind the socket to server address and server port
serverSocket.listen(1) #Listen to at most 1 connection at a time
while True: #while the following condition is true, run the function.
    #Establish the connection
    print('Ready to serve...')#Printing the message on to the console
    connectionSocket, addr = serverSocket.accept() #Accept the connection request and set up a new connection for the client
    try: #It tries the error and returns a message, instead of crashing the code when an error occurs.
        message = connectionSocket.recv(1024) #receives message from client print message filename = message.split()[1]
        filename = message.split()[1] #opens file and reads the contents
        f = open(filename[1:]) #to open a file in read mode
        outputdata = f.read() # We use the open function to create a file handler (f) # and then we use the file handler to read the content # of the file using the read() function.
        #Send one HTTP header line into socket
        connectionSocket.send(b'HTTP/1.0 200 OK\r\n\r\n') #prefixing the string with b, will convert the string to bytes
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)): #for if i is within the range, run the following function.
            connectionSocket.send(outputdata[i].encode())#returns an encoded version of the string
        connectionSocket.send("\r\n".encode()) #returns an encoded version of the string
        connectionSocket.close() #closes the connection socket connection
    except IOError: #message is printed, when an error occurs.
        #Send response message for file not found
        connectionSocket.send(b"HTTP/ 1.1 404 Not Found\r\n") #Sends a response message for file not found
        connectionSocket.send(b"\r\n") #line separator, prints the message on a new line
        connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n") #Displays a 404 Not Found message when a file requested is not found
        #Close client socket
        connectionSocket.close()  # closes the socket for the client
serverSocket.close()#closes the server socket connection
sys.exit() #Terminate the program after sending the corresponding data
