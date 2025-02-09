import socket

def client_program():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    
    while True:
        print("\nMenu:")
        print("1. Change case (swap) of a string")
        print("2. Evaluate a mathematical expression")
        print("3. Find the reverse of a string")
        print("4. Exit")
        
        option = input("Enter option: ")
        if option == '4':
            client.sendall("4:".encode())
            break
        
        value = input("Enter input: ")
        client.sendall(f"{option}:{value}".encode())
        response = client.recv(1024).decode()
        print(f"Server response: {response}")
    
    client.close()

if __name__ == "__main__":
    client_program()
