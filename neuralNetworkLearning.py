# layer 0: 256, 1: 64, 2: 4

import neuralNetwork
import copy  # importing "copy" for copy operations 
import time
from collections import Counter
# import msgRenuvable 
import sys

if sys.version_info > (3, 0):
	pass
	# Python 3 code in this block
else:
	print("Please restart it with python version 3...")
	sys.exit()
	# Python 2 code in this block

sys.path.append('./utility')
from utility import toFixed, copyObjNetwork, imgLogic, extrameListVal, log, warning, SaveObj, ls, TCom

# test
S = SaveObj("test.dat")
# telegram notifier usage
# TCom.send("Hi")

currentIter = 0  # only for progress bar
numb123 = 0
bestDetected = 0  # score of the best NeuralNetwork

def networkLearningIter(PrevIterNeuralNetwork = None, silent = False, images = None):
	NetworkList = []
	global numb123
	numb123 += 1 # it counter
	rightNetworkList = []
	rightNetworkSumValuesList = []
	for i in range(8):  # 8 random weight networks

		if PrevIterNeuralNetwork is None:
				Network = neuralNetwork.NeuralNetwork([256, 64, 8, 4], None, i)  # [256, 64, 4]  send img
		else:
				Network = copyObjNetwork(PrevIterNeuralNetwork)
				if i != 0:
					# Network.mutation(0.1, 0.1)
					Network.mutation(0.1, 0.2)

		sumQualityNetwork = 0
		# all photos send to neural network
		for k in images:
			Network.changeInputVals(k[1])
			calcRes = Network.showChosenLetter()
			if calcRes[0] == k[0]:
				rightNetworkList.append(int(i))
				sumQualityNetwork += Network.outputResQuality(k[0])
		NetworkList.append(copy.deepcopy(Network))
		NetworkList[len(NetworkList) - 1].initLayers(Network.returnLayers())  # hard copy of neurones Layers

		del Network

		rightNetworkSumValuesList.append(sumQualityNetwork)  # add sum for chosing best network is more networks weren't detected

	countedList = Counter(rightNetworkList)  # return [1: 5, a: 87, 3: 8]
	valsD = countedList.values()  # get val
	maxValues = max(valsD)

	rightNetworkSumValuesMaxList = []
	tmpList1 = []
	for key, val in countedList.items():  # return one key of element with max val
		if val == maxValues:
			rightNetworkSumValuesMaxList.append(key)

	log("network[" + '\033[92m' + str(key) + '\033[0m' + ']' + ',', "detected:", '\033[95m' + str(val))
	global preTime1
	log("Iter Time:", time.time() - preTime1)
	# D.log("progress: " + str(toFixed(currentIter/iterAmm * 100, 2)) + '%')
	for i in rightNetworkSumValuesMaxList:
		tmpList1.append(rightNetworkSumValuesList[i])  # best ammong sumQualityNetwork
		
	tmp123 = extrameListVal(tmpList1, False)  # return index of max element
	log("best sumQualityNetworks:", max(tmpList1))  
	# log("index:", rightNetworkSumValuesList.index(tmpList1[tmp123]))
	bestNeuralNetworkNumber = rightNetworkSumValuesList.index(tmpList1[tmp123])

	### crutch 04 04 19
	if val > 20:  # ssd saving
		import datetime
		timestr = f"{datetime.datetime.now():%Y-%m-%d %H_%M_%S_%f}"
		bestS = SaveObj("bestNetworks/" + str(val) + "_" + str(timestr) + ".dat")
		bestS.save(NetworkList[bestNeuralNetworkNumber])
	### crutch

	# send best score to my telegram
	global bestDetected
	if bestDetected < val:
		bestDetected = val
		log("New best result:", bestDetected)
		TCom.send("New best result: " + str(bestDetected))

	return copyObjNetwork(NetworkList[bestNeuralNetworkNumber])


def networkLearning(iterationAmmount = 100):
	
	global iterAmm  # only for progress bar
	iterAmm = iterationAmmount
	# a(10)b(10)c(10)d(10)
	# imgNamesList = ["a_1.png", "a_2.png", "a_3.png", "a_4.png", "a_5.png", "a_6.png", "a_7.png", "a_8.png", "a_9.png", "a_10.png", \
	# "b_1.png", "b_2.png", "b_3.png", "b_4.png", "b_5.png", "b_6.png", "b_7.png", "b_8.png", "b_9.png", "b_10.png", \
	# "c_1.png", "c_2.png", "c_3.png", "c_4.png", "c_5.png", "c_6.png", "c_7.png", "c_8.png", "c_9.png", "c_10.png", \
	# "d_1.png", "d_2.png", "d_3.png", "d_4.png", "d_5.png", "d_6.png", "d_7.png", "d_8.png", "d_9.png", "d_10.png"]

	# abcd(14)
	# imgNamesList = ["a_1.png", "b_1.png", "c_1.png", "d_1.png", "a_2.png", "b_2.png", "c_2.png", "d_2.png", "a_3.png", \
	# "b_3.png", "c_3.png", "d_3.png", "a_4.png", "b_4.png", "c_4.png", "d_4.png", "a_5.png", "b_5.png", "c_5.png", "d_5.png", \
	# "a_6.png", "b_6.png", "c_6.png", "d_6.png", "a_7.png", "b_7.png", "c_7.png", "d_7.png", "a_8.png", "b_8.png", "c_8.png", "d_8.png", \
	# "a_9.png", "b_9.png", "c_9.png", "d_9.png", "a_10.png", "b_10.png", "c_10.png", "d_10.png", "a_11.png", "b_11.png", "c_11.png", "d_11.png", \
	# "a_12.png", "b_12.png", "c_12.png", "d_12.png", "a_13.png", "b_13.png", "c_13.png", "d_13.png", "a_14.png", "b_14.png", "c_14.png", "d_14.png"]

	# abcde(14)
	imgNamesList = ["a_1.png", "b_1.png", "c_1.png", "d_1.png", "e_1.png", "a_2.png", "b_2.png", "c_2.png", "d_2.png", "e_1.png", "a_3.png", \
	"b_3.png", "c_3.png", "d_3.png", "e_1.png", "a_4.png", "b_4.png", "c_4.png", "d_4.png", "e_1.png", "a_5.png", "b_5.png", "c_5.png", "d_5.png", \
	"e_1.png", "a_6.png", "b_6.png", "c_6.png", "d_6.png", "e_1.png", "a_7.png", "b_7.png", "c_7.png", "d_7.png", "e_1.png", "a_8.png", "b_8.png", \
	"c_8.png", "d_8.png", "e_1.png", "a_9.png", "b_9.png", "c_9.png", "d_9.png", "e_1.png", "a_10.png", "b_10.png", "c_10.png", "d_10.png", \
	"e_1.png", "a_11.png", "b_11.png", "c_11.png", "d_11.png", "e_1.png", "a_12.png", "b_12.png", "c_12.png", "d_12.png", "e_1.png", "a_13.png", \
	"b_13.png", "c_13.png", "d_13.png", "e_1.png", "a_14.png", "b_14.png", "c_14.png", "d_14.png", "e_1.png"]

	# imgNamesList = ["a_1.png", "a_2.png", "b_1.png", "b_2.png", "c_1.png", "c_2.png", "d_1.png", "d_2.png"]

	log(imgNamesList)

	images = []
	MutantNetwork = None

	for n in imgNamesList:
		images.append([n[0], imgLogic(n)])

	for i in range(iterationAmmount):
		global currentIter  # only for progress bar
		currentIter = i
		log("current progress [" + str(numb123) + "]:", str(toFixed(currentIter/iterAmm * 100, 2)) + '%')

		res = None
		while res is None:
			preTime = time.time()
			res = networkLearningIter(MutantNetwork, True, images)  # get res of iter

			if res is not None:
				MutantNetwork = copyObjNetwork(res)
	return res

def networkTest(NeuralNetwork = None, iterationAmmount = 1):
	# imgNamesList = ["a_1.png", "a_2.png", "a_3.png", "a_4.png", "a_5.png", "a_6.png", "a_7.png", "a_8.png", "a_9.png", "a_10.png", \
	# "b_1.png", "b_2.png", "b_3.png", "b_4.png", "b_5.png", "b_6.png", "b_7.png", "b_8.png", "b_9.png", "b_10.png", \
	# "c_1.png", "c_2.png", "c_3.png", "c_4.png", "c_5.png", "c_6.png", "c_7.png", "c_8.png", "c_9.png", "c_10.png", \
	# "d_1.png", "d_2.png", "d_3.png", "d_4.png", "d_5.png", "d_6.png", "d_7.png", "d_8.png", "d_9.png", "d_10.png"]

	# imgNamesList = ["a_1.png", "a_2.png", "b_1.png", "b_2.png", "c_1.png", "c_2.png", "d_1.png", "d_2.png"]

	imgNamesList = ["a_1.png", "b_1.png", "c_1.png", "d_1.png", "a_2.png", "b_2.png", "c_2.png", "d_2.png", "a_3.png", \
	"b_3.png", "c_3.png", "d_3.png", "a_4.png", "b_4.png", "c_4.png", "d_4.png", "a_5.png", "b_5.png", "c_5.png", "d_5.png", \
	"a_6.png", "b_6.png", "c_6.png", "d_6.png", "a_7.png", "b_7.png", "c_7.png", "d_7.png", "a_8.png", "b_8.png", "c_8.png", "d_8.png", \
	"a_9.png", "b_9.png", "c_9.png", "d_9.png", "a_10.png", "b_10.png", "c_10.png", "d_10.png"]

	percentageForOne = 100.0 / len(imgNamesList)
	getPercentage = 0
	getPercentageA = 0
	getPercentageB = 0
	getPercentageC = 0
	getPercentageD = 0
	for n in imgNamesList:
		for m in range(iterationAmmount):

			# log(n, "iter:", m)
			
			pixels = imgLogic(n)
			NeuralNetwork.changeInputVals(pixels)

			# NeuralNetwork.showOutputNeurones()

			best = NeuralNetwork.showChosenLetter()
			if n[0] == best[0]:
				# print(True)
				getPercentage += percentageForOne
				if n[0] == "a":
					getPercentageA += percentageForOne
				elif n[0] == "b":
					getPercentageB += percentageForOne
				elif n[0] == "c":
					getPercentageC += percentageForOne
				elif n[0] == "d":
					getPercentageD += percentageForOne
			# NeuralNetwork.showChosenLetter(False)  # silent False
	print("Detected %:", getPercentage)
	print("a:", getPercentageA, "b:", getPercentageB, "c:", getPercentageC, "d:", getPercentageD)



#########################################################################################################
# learning
preTime1 = time.time()
# warning("warning test")
TrainedNetwork = copyObjNetwork(networkLearning(1000))
print("GEN Time:", time.time() - preTime1)

log("___ TEST FOR BEST NETWORK! ___")

# test loaded network
# NetFile = SaveObj("29_2019-04-04 14_53_02_906568.dat")  # 72.5 %
# NetFile = SaveObj("26_2019-04-05 10_57_45_687029.dat")  # 65.0 %
# NetFile = SaveObj("16_2019-04-05 10_29_47_830698.dat")  # 52.5 %

# TrainedNetwork = NetFile.load()
# networkTest(TrainedNetwork, 1)



# autotest
# strDir = "bestNetworks/experimental"
# filesList = ls(strDir)
# # print("ls", ls("bestNetworks/1"))
# for i in filesList:
# 	print(strDir + "/" + i)
# 	NetFile = SaveObj(strDir + "/" + i)  # ? %
# 	TrainedNetwork = NetFile.load()
# 	networkTest(TrainedNetwork, 1)
# 	print("------------")


# it works load/save
# S.save(TrainedNetwork)  # create an empty file for dbDataProc.py save
# neuralNetworkSerialized = S.load()
# log("Coppied neural network")
# neuralNetworkSerialized.showOutputNeurones()
