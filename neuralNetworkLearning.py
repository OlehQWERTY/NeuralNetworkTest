# layer 0: 256, 1: 64, 2: 4

import neuralNetwork
import copy  # importing "copy" for copy operations 
import time
from collections import Counter
# import msgRenuvable 
from utility import toFixed, copyObjNetwork, imgLogic, extrameListVal, Debug
D = Debug.getInstance()  # get debug obj

currentIter = 0  # only for progress bar
numb123 = 0

def networkLearningIter(PrevIterNeuralNetwork = None, silent = False, images = None):
	NetworkList = []
	global numb123
	numb123 += 1 # it counter
	rightNetworkList = []
	rightNetworkSumValuesList = []  # not tested
	for i in range(8):  # 8 random weight networks

		if PrevIterNeuralNetwork is None:
				Network = neuralNetwork.NeuralNetwork([256, 64, 8, 4], None, i)  # [256, 64, 4]  send img
		else:
				Network = copyObjNetwork(PrevIterNeuralNetwork)
				if i != 0:
					Network.mutation(0.1, 0.1)  # test

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

	D.log("network[" + '\033[92m' + str(key) + '\033[0m' + ']' + ',', "detected:", '\033[95m' + str(val))
	global preTime1
	D.log("Iter Time:", time.time() - preTime1)
	# D.log("progress: " + str(toFixed(currentIter/iterAmm * 100, 2)) + '%')
	for i in rightNetworkSumValuesMaxList:
		tmpList1.append(rightNetworkSumValuesList[i])  # best ammong sumQualityNetwork
		
	tmp123 = extrameListVal(tmpList1, False)  # return index of max element
	D.log("best sumQualityNetworks:", max(tmpList1))  
	# D.log("index:", rightNetworkSumValuesList.index(tmpList1[tmp123]))
	bestNeuralNetworkNumber = rightNetworkSumValuesList.index(tmpList1[tmp123])
	return copyObjNetwork(NetworkList[bestNeuralNetworkNumber])


def networkLearning(iterationAmmount = 100):
	
	global iterAmm  # only for progress bar
	iterAmm = iterationAmmount

	imgNamesList = ["a_1.png", "a_2.png", "a_3.png", "a_4.png", "a_5.png", "a_6.png", "a_7.png", "a_8.png", "a_9.png", "a_10.png", \
	"b_1.png", "b_2.png", "b_3.png", "b_4.png", "b_5.png", "b_6.png", "b_7.png", "b_8.png", "b_9.png", "b_10.png", \
	"c_1.png", "c_2.png", "c_3.png", "c_4.png", "c_5.png", "c_6.png", "c_7.png", "c_8.png", "c_9.png", "c_10.png", \
	"d_1.png", "d_2.png", "d_3.png", "d_4.png", "d_5.png", "d_6.png", "d_7.png", "d_8.png", "d_9.png", "d_10.png"]

	# imgNamesList = ["a_1.png", "a_2.png", "b_1.png", "b_2.png", "c_1.png", "c_2.png", "d_1.png", "d_2.png"]  # test

	D.log(imgNamesList)

	images = []
	MutantNetwork = None

	for n in imgNamesList:
		images.append([n[0], imgLogic(n)])

	for i in range(iterationAmmount):
		global currentIter  # only for progress bar
		currentIter = i
		D.log("current progress [" + str(numb123) + "]:", str(toFixed(currentIter/iterAmm * 100, 2)) + '%')

		res = None
		while res is None:
			preTime = time.time()
			res = networkLearningIter(MutantNetwork, True, images)  # get res of iter

			if res is not None:
				MutantNetwork = copyObjNetwork(res)
	return res

def networkTest(NeuralNetwork = None, iterationAmmount = 10):
	# imgNamesList = ["a_1.png", "a_2.png", "a_3.png", "a_4.png", "a_5.png", "a_6.png", "a_7.png", "a_8.png", "a_9.png", "a_10.png", \
	# "b_1.png", "b_2.png", "b_3.png", "b_4.png", "b_5.png", "b_6.png", "b_7.png", "b_8.png", "b_9.png", "b_10.png", \
	# "c_1.png", "c_2.png", "c_3.png", "c_4.png", "c_5.png", "c_6.png", "c_7.png", "c_8.png", "c_9.png", "c_10.png", \
	# "d_1.png", "d_2.png", "d_3.png", "d_4.png", "d_5.png", "d_6.png", "d_7.png", "d_8.png", "d_9.png", "d_10.png"]

	imgNamesList = ["a_1.png", "a_2.png", "b_1.png", "b_2.png", "c_1.png", "c_2.png", "d_1.png", "d_2.png"]

	for n in imgNamesList:
		for m in range(iterationAmmount):
			D.log(n, "iter:", m)
			pixels = imgLogic(n)
			NeuralNetwork.changeInputVals(pixels)
			NeuralNetwork.showOutputNeurones()


#########################################################################################################

preTime1 = time.time()
TrainedNetwork = copyObjNetwork(networkLearning(10))

# add save to file func()
# add save res to xcel file

# 	  a_1   a_2   a_3
# a   0.1   ...
# b   0.2   ...
# c   0.3   ...
# d   0.4   ...

print("GEN Time:", time.time() - preTime1)
D.log("___ TEST FOR BEST NETWORK! ___")
networkTest(TrainedNetwork)
