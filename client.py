import socket
import threading


RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'


def print_message(message, error=False, warning=False, success=False):
    if error:
        print(f"{RED}{message}{RESET}")
    elif warning:
        print(f"{YELLOW}{message}{RESET}")
    elif success:
        print(f"{GREEN}{message}{RESET}")
    else:
        print(message)


nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "NICK":
                client.send(nickname.encode("utf-8"))
            else:
                print(f"{YELLOW}{message}{RESET}")
        except:
            print(f"{RED}An error occured!{RESET}")
            client.close()
            break


def write():
    while True:
        message = f"{GREEN}{nickname}:{RESET} {input('')}"
        client.send(message.encode("utf-8"))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
