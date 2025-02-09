import socket
import threading
import multiprocessing

# Function to handle client requests
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Received from {addr}: {data}")
            
            option, value = data.split(':', 1)
            if option == '1':
                response = value.swapcase()
            elif option == '2':
                try:
                    response = str(eval(value))
                except Exception as e:
                    response = f"Error: {str(e)}"
            elif option == '3':
                response = value[::-1]
            elif option == '4':
                response = "Exit"
                conn.sendall(response.encode())
                break
            else:
                response = "Invalid option"
            
            conn.sendall(response.encode())
        except Exception as e:
            print(f"Error handling client {addr}: {str(e)}")
            break
    conn.close()

def single_process_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(2)
    print("Single-Process Server listening on port 12345...")
    
    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)

def multi_process_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(3)
    print("Multi-Process Server listening on port 12345...")
    
    while True:
        conn, addr = server.accept()
        process = multiprocessing.Process(target=handle_client, args=(conn, addr))
        process.start()

def multi_threaded_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(3)
    print("Multi-Threaded Server listening on port 12345...")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    server_type = input("Enter server type (single/multi-process/multi-threaded): ").strip().lower()
    if server_type == "single":
        single_process_server()
    elif server_type == "multi-process":
        multi_process_server()
    elif server_type == "multi-threaded":
        multi_threaded_server()
    else:
        print("Invalid server type.")