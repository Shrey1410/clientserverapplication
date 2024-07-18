import socket 
import threading
HOST='127.0.0.1'
PORT=1234 
LISTENER_LIMT=5
active_client=[] #list of all currently connected user
def listen_for_message(client, username):
    while 1:
        message=client.recv(2048).decode('utf-8')
        if message!='':
            final_msg=username+"~"+message
            send_messages_to_all(final_msg)
        else :
            print(f"The message send from client {username} is empty")

def send_message_to_client(message, client):
    client.sendall(message.encode("utf-8"))

def send_messages_to_all(message):
    for user in active_client:
        send_message_to_client(message,user[1])


# function to handle client
def hanndel_client(client):
    while True:
        username=client.recv(2048).decode('utf-8')
        if username!='':
            active_client.append((username, client))
            promt_msg="SERVER~"+f"{username}"+"added to chat"
            send_messages_to_all(promt_msg)
            break
        else :
            print("Client username is empty")
    threading.Thread(target=listen_for_message, args=(client, username)).start()


def main():
    # AF_INET : we are going to use IPv4 addressing
    # SOCK_STREAM : for TCP protocol
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST,PORT))
        print("Server is running")
    except :
        print(f"unable to bind to Host :{HOST} ans Port :{PORT}")
    # Set server limit 
    server.listen(LISTENER_LIMT)
    while True:
        client, address =server.accept()
        print(f"Successfully connnected to client HOST: {address[0]} PORT:{address[1]}")
        threading.Thread(target=hanndel_client, args=(client,)).start()
if __name__ =='__main__':
    print('running')
    main()