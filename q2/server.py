import socket
import threading
import multiprocessing
import time
import sys

def handle_client(conn, addr):
    # print(f"Connected by {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            # print(f"Received from {addr}: {data}")
            
            time.sleep(3)  # Simulating delay of 3 seconds
            response = data[::-1]  # Reverse the string
            
            conn.sendall(response.encode())
        except Exception as e:
            print(f"Error handling client {addr}: {str(e)}")
            break
    conn.close()

def single_process_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(100)
    print("Single-Process Server listening on port 12345...")
    
    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)

def multi_process_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(100)
    print("Multi-Process Server listening on port 12345...")
    
    while True:
        conn, addr = server.accept()
        process = multiprocessing.Process(target=handle_client, args=(conn, addr))
        process.start()

def multi_threaded_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(100)
    print("Multi-Threaded Server listening on port 12345...")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "single":
            single_process_server()
        elif sys.argv[1] == "multi-process":
            multi_process_server()
        elif sys.argv[1] == "multi-threaded":
            multi_threaded_server()
        else:
            print("Invalid server type.")
        sys.exit(0)
    else:
        choice = input("Run server? Enter type (single/multi-process/multi-threaded): ").strip().lower()
        if choice == "single":
            single_process_server()
        elif choice == "multi-process":
            multi_process_server()
        elif choice == "multi-threaded":
            multi_threaded_server()
        else:
            print("Invalid server type.")
