import pyttsx3
import socket
import re
from datetime import datetime


sock = socket.socket()
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'Voicebot'
token = 'oauth:xxxxx'
channel = '#lowhello'
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\Maxim RSI Harpo 22kHz"
sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))
togle = 0
s = 0
while True:
		try:
			resp = sock.recv(2048).decode('utf-8')
		except ConnectionAbortedError:
			continue
		if resp.startswith('PING'):
			sock.send("PONG\n".encode('utf-8'))
		try:
			name_usr = resp.split('#')[1].split(':')[0]
			msg = resp.split('#')[1].split(' :')[1]
			print(msg)
		except:
			continue
		print(name_usr,':',msg)
		converter = pyttsx3.init()
		converter.setProperty('rate', 150)
		converter.setProperty('volume', 0.3)
		converter.setProperty('voice', voice_id)

		if 'читай ники' in msg:
			togle = 1
			s = 1
		if 'не читай ники' in msg:
			s = 1
			togle = 0
			if s == 1:
				converter.say('Хорошо')
				s = 0
		if togle == 1:
			converter.say(name_usr + 'говорит' + msg)
		if s == 0 and 'не читай ники' not in msg:
			converter.say(msg)

		converter.runAndWait()

# voices = converter.getProperty('voices')
#
# for voice in voices:
#     # to get the info. about various voices in our PC
#     print("Voice:")
#     print("ID: %s" % voice.id)
#     print("Name: %s" % voice.name)
#     print("Age: %s" % voice.age)
#     print("Gender: %s" % voice.gender)
#     print("Languages Known: Ц%s" % voice.languages)
