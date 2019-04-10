# layer 0: 256, 1: 64, 2: 4

import neuralNetwork
import copy  # importing "copy" for copy operations 
import time
from collections import Counter
import sys

if sys.version_info > (3, 0):
	pass
	# Python 3 code in this block
else:
	log("Please restart it with python version 3...")
	sys.exit()
	# Python 2 code in this block

sys.path.append('./utility')
from utility import toFixed, copyObjNetwork, imgLogic, extrameListVal, log, warning, error, SaveObj, ls, TCom


class NeuralNetworkLearning:

	# singleton
	__instance = None
	__linesList = []


	@staticmethod 
	def getInstance():
		""" Static access method. """
		if NeuralNetworkLearning.__instance == None:
			NeuralNetworkLearning()
		return NeuralNetworkLearning.__instance


	def __init__(self):
		""" Virtually private constructor. """
		if NeuralNetworkLearning.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			NeuralNetworkLearning.__instance = self

		# not a part of singleton
		self.imgLists()  # make img list available from everywhere in this class
	# singleton

	TSilent = False  # don't send me telegram msg about new best score
	currentIter = 0  # only for progress bar
	bestDetected = 0  # score of the best NeuralNetwork
	startLearningTime = 0
	iterAmm  = 0  # only for progress bar


	def imgLists(self):

		######### networkLearningImgList #########

		# a(10)b(10)c(10)d(10)
		# self.networkLearningImgList = ["a_1.png", "a_2.png", "a_3.png", "a_4.png", "a_5.png", "a_6.png", "a_7.png", "a_8.png", "a_9.png", "a_10.png", \
		# "b_1.png", "b_2.png", "b_3.png", "b_4.png", "b_5.png", "b_6.png", "b_7.png", "b_8.png", "b_9.png", "b_10.png", \
		# "c_1.png", "c_2.png", "c_3.png", "c_4.png", "c_5.png", "c_6.png", "c_7.png", "c_8.png", "c_9.png", "c_10.png", \
		# "d_1.png", "d_2.png", "d_3.png", "d_4.png", "d_5.png", "d_6.png", "d_7.png", "d_8.png", "d_9.png", "d_10.png"]

		# abcd(14)
		# self.networkLearningImgList = ["a_1.png", "b_1.png", "c_1.png", "d_1.png", "a_2.png", "b_2.png", "c_2.png", "d_2.png", "a_3.png", \
		# "b_3.png", "c_3.png", "d_3.png", "a_4.png", "b_4.png", "c_4.png", "d_4.png", "a_5.png", "b_5.png", "c_5.png", "d_5.png", \
		# "a_6.png", "b_6.png", "c_6.png", "d_6.png", "a_7.png", "b_7.png", "c_7.png", "d_7.png", "a_8.png", "b_8.png", "c_8.png", "d_8.png", \
		# "a_9.png", "b_9.png", "c_9.png", "d_9.png", "a_10.png", "b_10.png", "c_10.png", "d_10.png", "a_11.png", "b_11.png", "c_11.png", "d_11.png", \
		# "a_12.png", "b_12.png", "c_12.png", "d_12.png", "a_13.png", "b_13.png", "c_13.png", "d_13.png", "a_14.png", "b_14.png", "c_14.png", "d_14.png"]

		# abcde(14)
		self.networkLearningImgList = ["a_1.png", "b_1.png", "c_1.png", "d_1.png", "e_1.png", "a_2.png", "b_2.png", "c_2.png", "d_2.png", "e_1.png", "a_3.png", \
		"b_3.png", "c_3.png", "d_3.png", "e_1.png", "a_4.png", "b_4.png", "c_4.png", "d_4.png", "e_1.png", "a_5.png", "b_5.png", "c_5.png", "d_5.png", \
		"e_1.png", "a_6.png", "b_6.png", "c_6.png", "d_6.png", "e_1.png", "a_7.png", "b_7.png", "c_7.png", "d_7.png", "e_1.png", "a_8.png", "b_8.png", \
		"c_8.png", "d_8.png", "e_1.png", "a_9.png", "b_9.png", "c_9.png", "d_9.png", "e_1.png", "a_10.png", "b_10.png", "c_10.png", "d_10.png", \
		"e_1.png", "a_11.png", "b_11.png", "c_11.png", "d_11.png", "e_1.png", "a_12.png", "b_12.png", "c_12.png", "d_12.png", "e_1.png", "a_13.png", \
		"b_13.png", "c_13.png", "d_13.png", "e_1.png", "a_14.png", "b_14.png", "c_14.png", "d_14.png", "e_1.png"]

		######### networkLearningImgList #########

		self.networkTestLearningImgList = ["a_1.png", "b_1.png", "c_1.png", "d_1.png", "a_2.png", "b_2.png", "c_2.png", "d_2.png", "a_3.png", \
		"b_3.png", "c_3.png", "d_3.png", "a_4.png", "b_4.png", "c_4.png", "d_4.png", "a_5.png", "b_5.png", "c_5.png", "d_5.png", \
		"a_6.png", "b_6.png", "c_6.png", "d_6.png", "a_7.png", "b_7.png", "c_7.png", "d_7.png", "a_8.png", "b_8.png", "c_8.png", "d_8.png", \
		"a_9.png", "b_9.png", "c_9.png", "d_9.png", "a_10.png", "b_10.png", "c_10.png", "d_10.png"]

		######### networkLearningImgList #########


	# telegram msg
	def Tmsg(self, val):
		if not self.TSilent:
			if self.bestDetected < val:
				self.bestDetected = val
				log("New best result:", self.bestDetected)
				TCom.send("New best result: " + str(self.bestDetected))


	def networkLearningIter(self, PrevIterNeuralNetwork = None, silent = False, images = None, ssdSavingNum = 0):
		NetworkList = []
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
		log("Iter Time:", time.time() - self.startLearningTime)
		# D.log("progress: " + str(toFixed(currentIter/self.iterAmm * 100, 2)) + '%')
		for i in rightNetworkSumValuesMaxList:
			tmpList1.append(rightNetworkSumValuesList[i])  # best ammong sumQualityNetwork
			
		tmp123 = extrameListVal(tmpList1, False)  # return index of max element
		log("best sumQualityNetworks:", max(tmpList1))  
		# log("index:", rightNetworkSumValuesList.index(tmpList1[tmp123]))
		bestNeuralNetworkNumber = rightNetworkSumValuesList.index(tmpList1[tmp123])

		### crutch 04 04 19
		if val > ssdSavingNum:  # ssd saving
			import datetime
			timestr = f"{datetime.datetime.now():%Y-%m-%d %H_%M_%S_%f}"
			bestS = SaveObj("bestNetworks/" + str(val) + "_" + str(timestr) + ".dat")
			bestS.save(NetworkList[bestNeuralNetworkNumber])  # serialize NeuralNetwork
		### crutch

		# send best score to my telegram
		self.Tmsg(val)

		return copyObjNetwork(NetworkList[bestNeuralNetworkNumber])


	def networkLearning(self, iterationAmmount = 100, ssdSavingNum = 0):
		
		self.iterAmm = iterationAmmount

		log(self.networkLearningImgList)

		images = []
		MutantNetwork = None

		for n in self.networkLearningImgList:
			images.append([n[0], imgLogic(n)])

		for i in range(iterationAmmount):
			# only for progress bar
			self.currentIter = i
			log("current progress [" + str(self.currentIter) +  "]:", str(toFixed(self.currentIter/self.iterAmm * 100, 2)) + '%')

			res = None
			while res is None:
				preTime = time.time()
				res = self.networkLearningIter(MutantNetwork, True, images, ssdSavingNum)  # get res of iter

				if res is not None:
					MutantNetwork = copyObjNetwork(res)
		return res

	def networkTest(self, NeuralNetwork = None):
		print(self.networkTestLearningImgList)
		percentageForOne = 100.0 / len(self.networkTestLearningImgList)
		getPercentage = 0
		getPercentageA = 0
		getPercentageB = 0
		getPercentageC = 0
		getPercentageD = 0
		for n in self.networkTestLearningImgList:
			
			pixels = imgLogic(n)
			NeuralNetwork.changeInputVals(pixels)

			# NeuralNetwork.showOutputNeurones()

			best = NeuralNetwork.showChosenLetter()
			if n[0] == best[0]:
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
		log("Detected %:", getPercentage)
		log("a:", getPercentageA, "b:", getPercentageB, "c:", getPercentageC, "d:", getPercentageD)


	def learning(self, iterations, ssdSavingNum = 0):
		self.startLearningTime = time.time()
		TrainedNetwork = copyObjNetwork(self.networkLearning(iterations, ssdSavingNum))
		log("GEN Time:", time.time() - self.startLearningTime)


	# test loaded network
	def testNetwork(self, filePath = None):
		if filePath:
			NetFile = SaveObj(filePath)
			TrainedNetwork = NetFile.load()  # deserialize NeuralNetwork
			log(filePath)
			self.networkTest(TrainedNetwork)
		else:
			error("File path doesn't specified!")


	# test all serialized networks in dir
	def testMultipleNetworks(self, dirPath = None):
		if dirPath:
			filesList = ls(dirPath)
			for i in filesList:
				log(dirPath + "/" + i)
				NetFile = SaveObj(dirPath + "/" + i) 
				TrainedNetwork = NetFile.load()  # deserialize NeuralNetwork
				self.networkTest(TrainedNetwork)
				print()  # empty line visual divide
		else:
			error("Dir path doesn't specified!")  # bug: "wrong path is showed" 



if __name__ == "__main__":
	A = NeuralNetworkLearning.getInstance()
	# A.learning(10, 20)
	# A.testNetwork("bestNetworks/experimental/29_2019-04-04 14_53_02_906568.dat")
	A.testMultipleNetworks("bestNetworks/experimental")
