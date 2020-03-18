""" corware.py default System Release is based on Windows 10

Project made by parad0x - snavellet - Carrots and Soy Sauce - DVisual

"""
import os # find system user-path
import platform # define Windows release
import sys # to import win version & auto-select virus
import time

def win_10_virus():
	import sys
	sys.path.insert('./corware')
	import win10_corware as win10
	print(win10.key())

def virus():
	import sys
	sys.path.insert('./corware')
	import win10_corware as virus
	print(virus.main())

# variables
win_ver = platform.system() + platform.release()

def what_windows_is_running(): # for testing, both Windows 10 viruses will be implemented on same versions
	# print(win_ver) // DEBUGGING
	if "10" in win_ver:
		win_10_virus()
		time.sleep(0.1)
		virus()
		pass
		# print("Windows 10 found") // DEBUGGING
	elif "7" in win_ver:
		win_10_virus()
		time.sleep(0.1)
		virus()
		# print("Windows 7 found") // DEBUGGING
		# find sys path for windows 7
		'''sys.path.insert(0, './corware')
		import win7_corware.py as win7
		print(win7.start(),main())'''
	else:
		exit()
		# print("Running corware (default)") // DEBUGGING
if __name__ == '__main__':
	what_windows_is_running()
