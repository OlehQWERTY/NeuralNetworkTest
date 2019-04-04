# autolaunch
import subprocess
import multiprocessing
import time
coresAmmount = multiprocessing.cpu_count()
print(coresAmmount, "cores is detected")

dictProc = {}
for i in range(coresAmmount):
	dictProc["proc" + str(i + 1)] = 0

for infin in range(10000):
	for i in range(multiprocessing.cpu_count()):
		print(i)
		dictProc[i] = subprocess.Popen(['python', 'main.py'])

	time.sleep(200)

	for i in range(multiprocessing.cpu_count()):
		print("kill:", i)
		dictProc[i].kill()