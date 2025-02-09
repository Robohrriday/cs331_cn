import socket
import time

def client_program():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    
    message = "Benchmarking Test String"
    # start_time = time.time()
    client.sendall(message.encode())
    
    response = client.recv(1024).decode()
    # end_time = time.time()
    
    # print(f"Reversed string from server: {response}")
    # print(f"Execution time: {end_time - start_time:.3f} seconds")
    
    client.close()

if __name__ == "__main__":
    client_program()
