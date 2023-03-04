#socket = connection between process (TCP Connections)
#in computer networking, an internet socket or network socket is an endpoint of a bidirectional
#inter-process communication flow across an internet protocol-based computer network
#such as the internet
#socket = cable that transmitt information from pc to pc

#TCP Port Numbers
#a port is an application-specific or process-specific
#software communications endpoint
#it allows multiple networked applications to coexist on the same server
#there is a list of well known TCP port numbers
#Telnet Login port 23
#SSH Secure login port 22
#HTTP port 80
#HTTPS Secure port 443
#SMTP mail port 25
#IMAP Mail Retrieval port 143/220/993
#POP Mail retrieval port 109/110
#DNS Domain Name port 53
#FTP File Transfer port 21

#lasi-asia.org/8080
#sometimes we see the port number in the URL if the web server is running on a "non-standard" port

#socket in python
#python has built-in support for TCP Socket
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
#data.pr4e.org is the host, 80 is the port