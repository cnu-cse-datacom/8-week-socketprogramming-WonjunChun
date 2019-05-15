#sender 역할
import socket
import os # 전송할 파일 크기 받기위해

FLAGS = None

ip_addr = '192.168.64.159' #나중에 채우기
port = 9000 #server의 포트 9000으로 보냄

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Input your file name : ")
socket.sendto(filename.encode(), (ip_addr, port))
filesize = str(os.path.getsize(filename)) # 타입에 맞게 바꿀것
socket.sendto(filesize.encode(), (ip_addr, port))
filesize =  int(filesize)

print("File Transmit Start....")
#socket.sendto(filename.encode(), (ip_addr, port))
sendfile = open(filename, 'rb') #binary로 전송
data = sendfile.read(1024)

send_size = 0
send_rate = 0
while len(data) != 0:
    send_size += len(data)
    send_rate = (send_size/filesize) * 100
    #data = sendfile.read(1024)
    socket.sendto(data, (ip_addr, port))
    data = sendfile.read(1024)
    print("current_size / total_size = " + str(send_size) + "/" + str(filesize) + ", " + str(send_rate) + "%")

print("ok")
print("file_send_end")
sendfile.close()
socket.close()
