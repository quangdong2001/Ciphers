import socket
import RC4
Key = "LITHUYETMATMA"
HOST = "192.168.1.133"
PORT = 2001
host_port = (HOST, PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(host_port)
    while True:
        fileName = input("Enter your file: File = ")
        f = open("Text.txt", 'rb')
        data_read = (f.read(1024)).decode("utf8")
        l = RC4.encrypt(Key, data_read)
        s.sendall(bytes(l,"utf8"))



        