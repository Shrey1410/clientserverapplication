import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
HOST='127.0.0.1'
PORT=1234
PR_BLUE="#003153"
SEL_BLUE="#007BA7"
BLUE="#00008B"
WHITE="white"
FONT=("Helvetica",17)
SMALL_FONT=("Helvetica",13)
BUTTON_FONT=("Helvetica",15)
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message+"\n")
    message_box.config(state=tk.DISABLED)
def connect():
    try:
        client.connect((HOST,PORT))
        # print("successfully connected to the server")
        add_message("Successfully connected to server")
    except:
        # print(f"unable to connect to server host :{HOST} Port :{PORT}")
        messagebox.showerror(f"unable to connect to server host :{HOST} Port :{PORT}")
        # exit(0)
    # username=input("enter username :")
    username=username_textbox.get()
    if username !='':
        client.sendall(username.encode())
    else :
        # print("uername cannot be empty")
        messagebox.showerror("Invalid username","uername cannot be empty")
        # exit(0)
    threading.Thread(target=listen_for_message_from_server, args=(client,)).start()
    username_textbox.config(state=tk.DISABLED)
    username_textbox.config(state=tk.DISABLED)

def send_message():
    # messages=input("Enter Message:")
    messages=message_textbox.get()
    if messages!='':
        client.sendall(messages.encode())
        message_textbox.delete(0, len(messages))
    else:
        # print("empty message")
        messagebox.showerror("Message cannot be empty")
        # exit(0)

root =tk.Tk()
root.geometry("600x600")
root.title("Messenger Client")
root.resizable(False,False)

root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=4)
root.grid_rowconfigure(2,weight=1)

top_frame=tk.Frame(root, width=600, height=100, bg=PR_BLUE)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)
middle_frame=tk.Frame(root, width=600, height=400, bg=SEL_BLUE)
middle_frame.grid(row=1, column=0, sticky=tk.NSEW)
bottom_frame=tk.Frame(root, width=600, height=100, bg=PR_BLUE)
bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

username_label=tk.Label(top_frame, text="Enter username: ", font=FONT, bg=PR_BLUE, fg=WHITE)
username_label.pack(side=tk.LEFT, padx=10)

username_textbox=tk.Entry(top_frame, font=BUTTON_FONT, bg=SEL_BLUE, fg=WHITE, width=23)
username_textbox.pack(side=tk.LEFT)

username_botton=tk.Button(top_frame, text="Join", font=FONT, bg=BLUE, fg=WHITE, command=connect)
username_botton.pack(side=tk.LEFT , padx=15)


message_textbox=tk.Entry(bottom_frame , font=FONT, bg=SEL_BLUE, fg=WHITE, width=38)
message_textbox.pack(side=tk.LEFT, padx=10)

message_button=tk.Button(bottom_frame, text="Send", font=BUTTON_FONT, bg=BLUE, fg=WHITE, command=send_message)
message_button.pack(side=tk.LEFT, padx=10)

message_box=scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=SEL_BLUE, fg=WHITE, width=67, height=26.5)
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)

def listen_for_message_from_server(client):
    while 1:
        message =client.recv(2048).decode("utf-8")
        if message!='':
            username =message.split('~')[0]
            content=message.split('~')[1]
            # print(f"{username}: {content}")
            add_message(f"[{username}] {content}")
        else :
            # print("message recieve from client a is empty")
            messagebox.showerror("message recieve from client a is empty")

# def communicate_server(client):
#     username=input("enter username :")
#     if username !='':
#         client.sendall(username.encode())
#     else :
#         print("uername cannot be empty")
#         exit(0)
#     threading.Thread(target=listen_for_message_from_server, args=(client,)).start()
#     sendmessage_to_server(client)

# def sendmessage_to_server(client):
#     while True:
#         messages=input("Enter Message:")
#         if messages!='':
#             client.sendall(messages.encode())
#         else:
#             print("empty message")
#             exit(0)

def main():
    root.mainloop()
    # communicate_server(client)

if __name__=='__main__':
    main()