# BruteForceCloud
A brute force client-server project.
1. client side using linux machine with airmon tools to capture WPA handshake, 
2. upload the pcap file to a Windows FTP server,
3. Windows server side uses Hashcat to brute force the password,
4. and sends back the password to the linux machine.
The project aviliable for now only for machines at the same network,
because of security issues that I didnt consider when coding thoose
right now I dont have much time to upgrade it but feel free to branch
your codes here.
