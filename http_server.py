import threading
import socket

def print_thread_func(argument):
    #while 1:
    print(argument)

def socket_server_thread_func():
    # Define socket host and port
    server_host = '0.0.0.0'
    server_port = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)
    while True:    
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024).decode()
        print(client_address)
        print(request)
        response = 'HTTP/1.0 200 OK\n\nHello World'
        client_connection.sendall(response.encode())
        client_connection.close()
    server_socket.close()


socket_server_thread = threading.Thread(target=socket_server_thread_func, name="socket_server_thread")
socket_server_thread.start()





socket_server_thread.join()

print_thread = threading.Thread(target=print_thread_func, name="print_thread", args=("heh",))
print_thread.start()
print_thread.join()


