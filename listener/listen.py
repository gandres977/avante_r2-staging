# client example

import socket, time
#client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client_socket.connect(('localhost', 5000))
#while True:
 #   time.sleep(5)
 #   data = client_socket.recv(512)
 #   if data.lower() == 'q':
 #       client_socket.close()
 #       break

 #   print("RECEIVED: %s" % data)
 #   data = input("SEND( TYPE q or Q to Quit):")
 #   client_socket.send(data)
 #   if data.lower() == 'q':
 #       client_socket.close()
 #       break
import socket
import csv
from datetime import datetime, timezone

def beaconToCSV(filename):
    inputFile = open(filename)
    data = inputFile.read().splitlines(True)
    # Remove the first line which includes IP/Port info for the socket connection used
    data = data[1:]
    outputFile = open(filename.split('.beacon')[0] +'.csv', 'w', newline='')
    csvWriter = csv.writer(outputFile)
    for line in data:
        print(line)
        list = line.split(',')
        print(list)
        csvWriter.writerow(list)
    outputFile.close()


s = socket.socket()
#host = socket.gethostname()
host = '192.168.10.249'
port = 5001
s.bind((host,port))
s.listen(5)
while True:
    c, addr = s.accept()
    msg1 = "Connection accepted from "
    print(msg1.encode() + repr(addr[1]).encode())
    utcnow = datetime.now(tz=timezone.utc).timestamp()
    beaconFileName = str(utcnow) + '.beacon'
    beaconFile = open(beaconFileName, 'w')
    beaconFile.write(str(addr[0]) + ',' + str(addr[1]) + '\n')
    msg2 = "Server approved connection"
    c.send(msg2.encode())
    socketMsg = c.recv(1026)
    if not socketMsg:
        break
    decodedMsg = socketMsg.decode()
    print(repr(addr[1]) + ": " + decodedMsg)
    beaconFile.write(decodedMsg)
    beaconFile.close()
    c.close()
    beaconToCSV(beaconFileName)




