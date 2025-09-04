import socket
import RC4
Key = "LITHUYETMATMA"
HOST = "192.168.1.133"
PORT = 2001
host_port = (HOST, PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(host_port)
    s.listen(10)
    while True:
        client, addr = s.accept()
        with client:
            print(f"Connected with port {addr[1]}")
            print("Server listenning...")
            while True:
                data_real = client.recv(1024)
                data_real1 = data_real.decode("utf8")
                print(f"Data is received from client: Data = {data_real1}")
                data_real2 = RC4.decrypt(Key, data_real1)
                print(f"Data is decrypted: Data = {data_real2}" )





