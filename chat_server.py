import socket, threading

clients = {}
lock = threading.Lock()

def handle_client(client, addr):
    try:
        username = client.recv(1024).decode().strip()
        with lock:
            clients[client] = username
        broadcast(f"{username} has joined the chat.", client)
        
        while True:
            msg = client.recv(1024).decode()
            if msg:
                broadcast(f"{username}@server: {msg}", client)
            else:
                break
    except:
        pass
    finally:
        with lock:
            if client in clients:
                broadcast(f"{clients[client]} has left the chat.", client)
                del clients[client]
        client.close()

def broadcast(msg, sender=None):
    with lock:
        for client in clients:
            if client != sender:
                try:
                    client.send(msg.encode() + b'\n')
                except:
                    pass

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 1234))
server.listen()
print("Server listening on port 1234...")

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client, addr)).start()
