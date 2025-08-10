from socket import *
import sys

def run_client(server_ip, server_port):
    # Create a TCP socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    
    try:
        # Connect to the server
        clientSocket.connect((server_ip, server_port))
        print(f"Connected to server {server_ip}:{server_port}")
        
        messages = []  # Store all sent/received messages
        
        while True:
            # Get user input
            message = input("Enter a message (or 'quit' to exit): ")
            clientSocket.send(message.encode())
            print(f"Sent to server: {message}")
            
            if message.lower() == "quit":
                break
            
            # Set timeout to prevent deadlock
            clientSocket.settimeout(5.0)
            
            try:
                data = clientSocket.recv(1024)
                if not data:
                    break
                    
                received_message = data.decode()
                messages.append(received_message)  # Fixed: was message.append
                print(f"Received from server: {received_message}")
                
                if received_message.lower() == "quit":
                    break
                    
            except timeout:
                continue
                
        clientSocket.close()
        print(f'Connection with server {server_ip}:{server_port} closed')
        
        # Print message log
        print("\nMessage Log:")
        for msg in messages:
            print(msg)
            
    except ConnectionRefusedError:
        print(f"Failed to connect to server {server_ip}:{server_port}")

def main():
    if len(sys.argv) == 3:
        server_ip = sys.argv[1]
        server_port = int(sys.argv[2])
    else:
        server_ip = input("Enter the server's IP address: ")
        server_port = int(input("Enter the server's port: "))
    
    run_client(server_ip, server_port)

if __name__ == "__main__":
    main()
