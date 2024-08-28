
import socket

def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 65432))

        a = input("Enter first number: ")
        operator = input("Enter operator (+, -, *, /): ")
        b = input("Enter second number: ")

        s.sendall(f"{a} {operator} {b}".encode())
        data = s.recv(1024)

    print(f"Result: {data.decode()}")

if __name__ == "__main__":
    run_client()
