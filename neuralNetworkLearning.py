# layer 0: 256, 1: 64, 2: 4

import neuralNetwork
import copy  # importing "copy" for copy operations 
import time
from collections import Counter
# import msgRenuvable 
from utility import toFixed, copyObjNetwork, imgLogic, extrameListVal, Debug

currentIter = 0  # only for progress bar
numb123 = 0

log = Debug(True)

log.log("123", __name__)

def networkLearningIter(PrevIterNeuralNetwork = None, silent = False, images = None):
	NetworkList = []
	global numb123
	numb123 += 1 # it counter
	rightNetworkList = []
	rightNetworkSumValuesList = []  # not tested
	for i in range(8):  # 8 random weight networks

		# from pympler.tracker import SummaryTracker
		# tracker = SummaryTracker()


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
				# Network.outputResQuality()
				# print(Network.outputResQuality(k[0]))
				# rightNetworkValuesList.append(calcRes)  # save right letter val
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
			# if key != 0:  # show changing
			print(numb123, " ____________")
			print("network:", key, "detected:", val)
			global preTime1
			print("Iter Time:", time.time() - preTime1)
			print("progress: " + str(toFixed(currentIter/iterAmm * 100, 2)) + '%')
			# 	# s.addLine(str(numb123) + " ____________")
			# s.addLine("network: " + str(key) + " detected: " + str(val))
			# 	# s.addLine(str(preTime1))
			# s.addLine("Iter Time: " + str(time.time() - preTime1))

			# s.addLine("progress: " + str(toFixed(currentIter/iterAmm * 100, 2)) + '%')
			# s.show(True)
			# else:  # best network is # [0], so choose one according to correct neurones val
			# 	key = extrameListVal(rightNetworkSumValuesList, False)  # return index of max element
			# 	print(rightNetworkSumValuesList)
			# 	print("approximation key =", key)
			# 	print("approximation val =", rightNetworkSumValuesList[key])
			# bestNeuralNetworkNumber = key
			# break
			# print(key)
			rightNetworkSumValuesMaxList.append(key)

	print("rightNetworkSumValuesList", rightNetworkSumValuesList)
	print("rightNetworkSumValuesMaxList", rightNetworkSumValuesMaxList)
	for i in rightNetworkSumValuesMaxList:
		# print(tmpList1)
		tmpList1.append(rightNetworkSumValuesList[i])
		print("tmpList1.append(rightNetworkSumValuesList[i])", rightNetworkSumValuesList[i])

	tmp123 = extrameListVal(tmpList1, False)
	print("max", tmp123)  # return index of max element

	print("index:", rightNetworkSumValuesList.index(tmpList1[tmp123]))

	bestNeuralNetworkNumber = rightNetworkSumValuesList.index(tmpList1[tmp123])
	# bestNeuralNetworkNumber = key
	# tracker.print_diff()

	# print("NetworkList", len(NetworkList))
	# print("rightNetworkValuesList", len(rightNetworkValuesList))
	# print("bestNeuralNetworkNumber", bestNeuralNetworkNumber%8)
	return copyObjNetwork(NetworkList[bestNeuralNetworkNumber])


def networkLearning(iterationAmmount = 10):
	
	global iterAmm  # only for progress bar
	iterAmm = iterationAmmount

	imgNamesList = ["a_1.png", "a_2.png", "a_3.png", "a_4.png", "a_5.png", "a_6.png", "a_7.png", "a_8.png", "a_9.png", "a_10.png", \
	"b_1.png", "b_2.png", "b_3.png", "b_4.png", "b_5.png", "b_6.png", "b_7.png", "b_8.png", "b_9.png", "b_10.png", \
	"c_1.png", "c_2.png", "c_3.png", "c_4.png", "c_5.png", "c_6.png", "c_7.png", "c_8.png", "c_9.png", "c_10.png", \
	"d_1.png", "d_2.png", "d_3.png", "d_4.png", "d_5.png", "d_6.png", "d_7.png", "d_8.png", "d_9.png", "d_10.png"]

	# imgNamesList = ["a_1.png", "a_2.png", "b_1.png", "b_2.png", "c_1.png", "c_2.png", "d_1.png", "d_2.png"]  # test

	# imgNamesList = ["a_1.png", "b_1.png", "a_2.png", "b_2.png", "a_3.png", "b_3.png", "a_4.png", "b_4.png", "a_5.png", "b_5.png"]
	images = []
	MutantNetwork = None

	for n in imgNamesList:
		images.append([n[0], imgLogic(n)])
		print(n)

	for i in range(iterationAmmount):
		global currentIter  # only for progress bar
		currentIter = i

		print("current progress: " + str(toFixed(currentIter/iterAmm * 100, 2)) + '%')

		# s.addLine("current progress: " + str(toFixed(currentIter/iterAmm * 100, 2)) + '%')
		# s.show()
		# s.clearLines(-1)
# 
		res = None
		while res is None:
			preTime = time.time()
			res = networkLearningIter(MutantNetwork, True, images)  # get res of iter

			if res is not None:
				MutantNetwork = copyObjNetwork(res)
	return res



#########################################################################################################
d = Debug(True)
d.log("koko123")

preTime1 = time.time()

# s = msgRenuvable.Singleton.getInstance()  # show lines and clear screen

# s.addLine("pretime: " + str(preTime1))

tmp1 = copyObjNetwork(networkLearning(1000))


print("++++++++++++++++++++++++++")

print("a_1.png")
pixels = imgLogic("a_1.png")
tmp1.changeInputVals(pixels)
tmp1.showOutputNeurones()

print("a_2.png")
pixels = imgLogic("a_2.png")
tmp1.changeInputVals(pixels)
tmp1.showOutputNeurones()

print("b_1.png")
pixels = imgLogic("b_1.png")
tmp1.changeInputVals(pixels)
tmp1.showOutputNeurones()

print("b_2.png")
pixels = imgLogic("b_2.png")
tmp1.changeInputVals(pixels)
tmp1.showOutputNeurones()

print("d_2.png")
pixels = imgLogic("d_2.png")
tmp1.changeInputVals(pixels)
tmp1.showOutputNeurones()


print("GEN Time:", time.time() - preTime1)
