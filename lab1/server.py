import socket

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    data = conn.recv(1024).decode()
    if not data:
        return

    a, operator, b = data.split()
    a = float(a)
    b = float(b)

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a / b
    else:
        result = "Invalid operator"

    conn.sendall(str(result).encode())
    conn.close()

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 65432))
    server.listen()

    print("Server is listening...")

    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)

if __name__ == "__main__":
    run_server()
