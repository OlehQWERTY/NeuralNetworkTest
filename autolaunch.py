# autolaunch some script in some ammount of threads

import sys

if sys.version_info > (3, 0):
	pass
	# Python 3 code in this block
else:
	print("Please restart it with python version 3...")
	sys.exit()
	# Python 2 code in this block


import os
import subprocess
import multiprocessing
import time

learningTime = 0.5  # in hours
coolDownTime = 60  # in sec


# differend python/python3 command for windows and ubuntu
if os.name == 'posix':
	pyCommand = 'python3'  # python3 - Ubuntu
else:
	pyCommand = 'python'  # python - Windows


coresAmmount = int(multiprocessing.cpu_count()/2 - 1) # -1 in order to have normal performanse for avarage usage
# coresAmmount = 2
print(coresAmmount, "threads is started")


dictProc = {}
for i in range(coresAmmount):
	dictProc["proc" + str(i + 1)] = 0

for infin in range(4):  # ~ 8 (32) hours of work
	for i in range(coresAmmount):
		# python - windows and ubuntu - python3 command
		dictProc[i] = subprocess.Popen([pyCommand, 'main.py'])  # python3 - Ubuntu

	time.sleep(learningTime * 3600)  # seconds of work  3600 - 60*60 seconds in 1 hour

	for i in range(coresAmmount):
		print("kill:", i)
		dictProc[i].kill()

	print("Cool down time")
	time.sleep(coolDownTime)  # cool down time