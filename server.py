import socket
import threading

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))  # Bind to IP and port
server_socket.listen(1)  # Listen for 1 connection

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received: {message}")
                # Broadcast message to all clients
                for client in clients:
                    if client != client_socket:
                        client.send(message.encode('utf-8'))
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server():
    print("Server is running...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
