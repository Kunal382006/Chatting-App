import socket
import tkinter as tk
from tkinter import messagebox
import threading

# Function to send message
def send_message():
    message = message_entry.get()
    if message != "":
        client_socket.send(message.encode('utf-8'))
        message_entry.delete(0, tk.END)

# Function to receive messages from the server
def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            chat_box.insert(tk.END, f"Friend: {message}\n")
        except:
            break

# Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))  # Connect to server

# Set up the GUI window
window = tk.Tk()
window.title("Chat App")

chat_box = tk.Text(window, height=15, width=50)
chat_box.pack()

message_entry = tk.Entry(window, width=40)
message_entry.pack(padx=10, pady=5)

send_button = tk.Button(window, text="Send", width=15, command=send_message)
send_button.pack()

# Start thread to receive messages
thread = threading.Thread(target=receive_message)
thread.daemon = True
thread.start()

# Run the GUI loop
window.mainloop()
