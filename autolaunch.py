# autolaunch
import sys

if sys.version_info > (3, 0):
	pass
	# Python 3 code in this block
else:
	print("Please restart it with python version 3...")
	sys.exit()
	# Python 2 code in this block



import subprocess
import multiprocessing
import time
coresAmmount = multiprocessing.cpu_count()
# coresAmmount = 2
# print(coresAmmount, "cores is detected")

dictProc = {}
for i in range(coresAmmount):
	dictProc["proc" + str(i + 1)] = 0

for infin in range(4):  # ~ 8 (32) hours of work
	for i in range(coresAmmount):
		print(i)
		dictProc[i] = subprocess.Popen(['python', 'main.py'])  # python3 - Ubuntu

	time.sleep(4000)  # ~ 16 (1000) min of work

	for i in range(coresAmmount):
		print("kill:", i)
		dictProc[i].kill()

	print("Cool down time")
	time.sleep(60)  # 60 s of cool down