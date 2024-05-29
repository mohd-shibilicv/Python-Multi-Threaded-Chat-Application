import socket
import threading


clients = []
nicknames= []

def broadcast(message):
    for client in clients:
        client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode("utf-8"))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        broadcast(f"Connected with {str(address)}".encode("utf-8"))

        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        print(f"New client joined: {nickname}")
        broadcast(f"{nickname} joined the chat!".encode("utf-8"))
        client.send("Connected to the server!".encode("utf-8"))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


host = "127.0.0.1"
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print(f"Server stated on {host}:{port}")
receive()
