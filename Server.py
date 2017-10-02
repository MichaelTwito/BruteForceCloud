import os
import socket
import sys

#This version support only Windows OS.

client_ip = raw_input("Enter Client IP: ")      #Setup the settings.
crunch = raw_input("Enter crunch location: ")
hashcat = raw_input("Enter hashcat location: ")
dst = raw_input("Enter the FTP dir: ")
def init():
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0',5013))
    server_socket.listen(1)
    (client_socket, client_address) = server_socket.accept()
    return client_socket.recv(1024)
    client_socket.send('' + client_name)
    client_socket.close()
    server_socket.close()

def convert_input():
    data = init()
    data = data.split(',')
    digit_0 = int(data[0])
    digit_f = int(data[1])
    string = ""
    for i in range(digit_0,digit_f+1):
        string = string + str(i)
    return data,string

def send_result(output,client_ip):
    send_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    send_socket.connect((client_ip, 1903))
    send_socket.send(str(output))
    send_socket.close()

data,alphabeta = convert_input()
print data
print client_ip
os.system(crunch + '\crunch.exe ' + data[2] +  " " + data[3] + " " + alphabeta + ' -t 050@@@@@@@ >' + crunch +'\passwords.txt')
os.system(hashcat + '\hashcat64.exe -m 2500 '+ dst +'\wpa.hccap ' +  crunch + '\passwords.txt --show > ' + hashcat + 'output.txt')
file = open( dst + '\hashcat-3.20output.txt','rb')
output = file.read(1024)
send_result(output,client_ip)
