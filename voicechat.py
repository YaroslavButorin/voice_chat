import pyttsx3
import socket


sock = socket.socket()
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'Voicebot'
token = 'oauth:wfuce3peq6cdfb0gd5442vcm1951nk'
channel = '#lowhello'
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\Maxim RSI Harpo 22kHz"
sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

while True:
		resp = sock.recv(2048).decode('utf-8')
		msg = resp.split(':')[-1]
		print(msg)
		converter = pyttsx3.init()
		converter.setProperty('rate', 150)
		converter.setProperty('volume', 10)
		converter.setProperty('voice', voice_id)
		converter.say(msg)
		converter.runAndWait()
#voices = converter.getProperty('voices')

# for voice in voices:
#     # to get the info. about various voices in our PC
#     print("Voice:")
#     print("ID: %s" % voice.id)
#     print("Name: %s" % voice.name)
#     print("Age: %s" % voice.age)
#     print("Gender: %s" % voice.gender)
#     print("Languages Known: %s" % voice.languages)