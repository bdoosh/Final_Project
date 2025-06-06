# get client request to open html
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 12345

server.bind((host, port))
server.listen()

while True:
    print(f"Listening on [{host}:{port}]")
    client, caddress = server.accept()
    
    print(f"Connected to {caddress}")
    request = client.recv(1024).decode()
    
    # If request to open index.html file
    if request:
        try:
            with open("index.html", "r") as file:
                html = file.read()
                client.sendall(b"HTTP/1.1 200 OK\r\n")
                
        # if file not found send 404 error
        except FileNotFoundError:
            html = "<html><body><h1>404 Not Found</h1></body></html>"
            client.sendall(b"HTTP/1.1 404 Not Found\r\n")
