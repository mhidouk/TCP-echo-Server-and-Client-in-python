# TCP-echo-Server-and-Client-in-python
# TCP Echo Server & Client in Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Network](https://img.shields.io/badge/Protocol-TCP-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A lightweight TCP echo server and client demonstrating socket programming fundamentals.

## 📦 Files
| File | Description |
|------|-------------|
| `server.py` | TCP server that echoes received messages |
| `client.py` | TCP client for interacting with the server |

## 🚀 Quick Start

1. **Start the server**:
   ```bash
   python server.py 12345
2. **Connect client**:
   python client.py localhost 12345

🛠️ Features
Bi-directional communication using TCP sockets
Multi-client support (sequential connections)
Graceful shutdown via quit command
Error handling for connection issues
Port configurability via command line

💻 Example Session
Server Terminal:

bash
$ python server.py 12345
Server started on 0.0.0.0:12345
Connected to client at 127.0.0.1:54321
Received: Hello World
Received: quit
Client Terminal:

bash
$ python client.py localhost 12345
> Hello World
Server replied: Hello World
> quit
Connection closed

📚 Technical Details
Protocol: TCP (SOCK_STREAM)
Address Family: IPv4 (AF_INET)
Buffer Size: 1024 bytes
Port Range: 1024-65535 (privileged ports require admin)

⚠️ Troubleshooting
Address already in use? Try different port
Connection refused? Verify server is running
Invalid port? Use number between 1024-65535
   
