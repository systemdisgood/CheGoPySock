import threading
import socket
import time

class ServerJsonHTTP:
    OKresponse = 'HTTP/1.0 200 OK\n\n'
    server_host = '0.0.0.0'
    def __init__(self, server_port = 8080) -> None:
        self.shell_run = True
        self.server_port = server_port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.server_host, self.server_port))
        self.server_socket.listen(1) 
        pass
    
    def server_thread_init(self):
        while self.shell_run:    
            self.client_connection, client_address = self.server_socket.accept()
            self.request = self.client_connection.recv(1024).decode()
            print(client_address)
            print(self.request)
            response = 'HTTP/1.0 200 OK\n\nHello World'
            self.client_connection.sendall(response.encode())
            self.client_connection.close()

    def server_stop(self):
        self.shell_run = False
        self.server_socket.close()
        self.socket_server_thread.join()

    
    def server_thread_run(self):
        self.socket_server_thread = threading.Thread(target=socket_server_thread_func, name="socket_server_thread")
        self.socket_server_thread.start()



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


ser = ServerJsonHTTP()
ser.server_thread_init()
ser.server_thread_run()

#time.sleep(5)
ser.server_stop()

#socket_server_thread = threading.Thread(target=socket_server_thread_func, name="socket_server_thread")
#socket_server_thread.start()





#socket_server_thread.join()

print_thread = threading.Thread(target=print_thread_func, name="print_thread", args=("heh",))
print_thread.start()
print_thread.join()


