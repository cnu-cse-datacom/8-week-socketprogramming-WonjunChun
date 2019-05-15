# server는 receiver 역할
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 9000))
data, addr = server_socket.recvfrom(1024)


print("file recv start from ", addr[0])
filename = data.decode()
print("File Name : ", filename) #data를 decode하면 파일명 나옴
filesize, addr = server_socket.recvfrom(1024)
filesize = int(filesize)
print("File Size : ", filesize) #filesize정보

received_size = 0 #현재 받은 사이즈
received_rate = 0 #받은 비율
received_file = open(filename, 'wb')#received_file에 받은 정보를 binary로 씀

data = server_socket.recv(1024)
while data: #받아온 데이터가 존재하는 경우
    received_file.write(data) #받아온 파일 씀
    received_size += int(len(data))
    #print(str(received_rate))
    received_rate = (received_size / filesize) * 100
    print("current_size / total_size = " + str(received_size) + "/" + str(filesize) + ", " + str(received_rate) + "%")
    data = server_socket.recv(1024)
    if len(data) == 0:
        break

received_file.write(data) #write last data
print("current_size / total_size = " + str(received_size) + "/" + str(filesize) + ", " + str(received_rate) + "%")

received_file.close()
server_socket.close()
