import socket

def connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.56.102",8080))
    s.listen(1)
    conn, addr = s.accept()
    print '[+] Got connection from: ', addr
    

    while True:
     
         password = conn.recv(1024)
         print password
         if not password: break
         
    conn.close()

def main():
    connect()
main()
