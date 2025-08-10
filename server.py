"""
server.py - TCP Chat Server

A Python script that acts as the server for the Many-to-Many Chat System.
Listens for client connections and echoes received messages back to clients.
"""

import socket
import sys

def run_server(port):
    """
    Run the chat server on the specified port.
    
    Args:
        port (int): The port number to listen on.
    """
    # Create TCP socket using IPv4
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get host information
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Server started on {ip_address}:{port}")
    
    try:
        # Bind to all interfaces and listen
        serverSocket.bind(('0.0.0.0', port))
        print(f'Server is listening on port {port}')
        serverSocket.listen(1)
        
        # Accept client connection
        clientSocket, clientAddress = serverSocket.accept()
        print(f"Connected to client at {clientAddress[0]}:{clientAddress[1]}")
        
        received_messages = []  # Store all received messages
        
        while True:
            # Receive and process client messages
            data = clientSocket.recv(1024).decode()
            if not data:
                break
                
            print(f"Received from client: {data}")
            received_messages.append(data)  # Fixed typo: was 'recieved_messages'
            
            if data.lower() == 'quit':
                print("Client requested to quit.")
                break
                
            # Echo messages back to client
            for message in received_messages:
                clientSocket.send(message.encode())
                
    except KeyboardInterrupt:
        print("\nServer stopped by administrator.")
    finally:
        clientSocket.close()
        serverSocket.close()
        print("Server socket closed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
        sys.exit(1)
        
    try:
        port = int(sys.argv[1])
        run_server(port)
    except ValueError:
        print("Error: Port must be a valid integer.")
        sys.exit(1)
