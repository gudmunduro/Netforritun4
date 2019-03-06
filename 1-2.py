import socket
import sys

try:
    url = input("URL: ")
    host = url.split("/")[2]
    print("host: " + host)
except:
    print("Invalid URL")
    sys.exit(1)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
mysock.send(bytes('GET ' + url + ' HTTP/1.0\r\n\r\n', 'utf-8'))

fullData: str = ''

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    fullData += str(data)

if len(fullData) > 3000:
    print("Data is more than 3000 characters")
    print(fullData[:3000])
else:
    print("Data is less than 3000 characters")
    print(fullData)

mysock.close()