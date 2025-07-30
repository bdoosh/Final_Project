# Get client request to open html
import socket

def run_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(1)
    print(f"Listening on [{host}:{port}]")

    while True:
        connection, caddress = server.accept()
        print(f"Connected to {caddress}")
        request = connection.recv(1024).decode('utf-8')
        string_list = request.split(' ')
        
        if len(string_list) < 2: # Check if request is valid
            print("Invalid request received.")
            connection.close()
            continue
        
        requested_file = string_list[1]

        print(f"Requested file: {requested_file}")
        my_file = requested_file.split('?')[0]  # Get the file name from request
        my_file = my_file.lstrip('/')
        
        if my_file == '':
            my_file = 'index.html'
        try:
            file = open(my_file, 'rb') # Open and read file in bi mode
            html = file.read()
            file.close()
            header = 'HTTP/1.1 200 OK\n'
                
            if my_file.endswith(".css"):
                mime_type = 'text/css'
            else:
                mime_type = 'text/html'
                
            header += f'Content-Type: {mime_type}\n'
            
        except Exception as e: # If file not found send 404 error
            html = b"<html><body><h1>Error 404</h1><h3>File not found</h3></body></html>"
            header = "HTTP/1.1 404 Not Found\n"
        
        response = header.encode('utf=8')
        response += html
        connection.send(response)
        connection.close()
        print("Response sent! Connection closed.\n")


if __name__ == "__main__":
    run_server('localhost', 12345)