import socket
from threading import Thread

nickname=input("Enter name ")
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipadress="127.0.0.1"
port=8000

client.connect((ipadress, port))
print("connected with server. :)")

def recieve():
    while True:
        try:
            message=client.recv(2048).decode("utf-8")
            if message=="NICKNAME":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            print("Error 404")
            client.close()
            break

def write():
    while True:
        message="{}:{}".format(nickname, input(""))
        client.send(message.encode("utf-8"))

recievethread=Thread(target=recieve)
recievethread.start()

writethread=Thread(target=write)
writethread.start()