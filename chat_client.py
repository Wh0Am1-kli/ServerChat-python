import socket
import threading
import os

def get_username():
    file_path = ".username"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return f.read().strip()
    else:
        username = input("Enter your username: ").strip()
        with open(file_path, "w") as f:
            f.write(username)
        return username

def receive(sock):
    while True:
        try:
            data = sock.recv(1024).decode()
            if data:
                print(data)
        except:
            break

host = input("Server IP: ").strip()
port = int(input("Port: ").strip())
username = get_username()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.send(username.encode())

threading.Thread(target=receive, args=(sock,), daemon=True).start()

while True:
    try:
        msg = input()
        if msg:
            sock.send(msg.encode())
    except KeyboardInterrupt:
        print("\nDisconnected.")
        sock.close()
        break
