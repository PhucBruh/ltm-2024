import socket
import tkinter as tk
from tkinter import messagebox

def calculate():
    a = entry_a.get()
    operator = entry_operator.get()
    b = entry_b.get()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 65432))
        s.sendall(f"{a} {operator} {b}".encode())
        result = s.recv(1024).decode()

    messagebox.showinfo("Result", f"The result is: {result}")

# GUI setup
root = tk.Tk()
root.title("TCP Calculator Client")

tk.Label(root, text="First Number:").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Operator (+, -, *, /):").grid(row=1, column=0)
entry_operator = tk.Entry(root)
entry_operator.grid(row=1, column=1)

tk.Label(root, text="Second Number:").grid(row=2, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

root.mainloop()
