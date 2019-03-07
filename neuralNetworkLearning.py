# layer 0: 256, 1: 64, 2: 4
import cv2
import numpy as np
import neuralNetwork
import copy  # importing "copy" for copy operations 
import time
from collections import Counter

numb123 = 0
# make it possible to use with different params ammount
# def a_decorator_debug(function_to_decorate):
# 	def a_wrapper_accepting_arguments(arg1, arg2, arg3):
# 		from pympler.tracker import SummaryTracker
# 		tracker = SummaryTracker()
# 		# print("Смотри, что я получил:", arg1, arg2, arg3)
# 		function_to_decorate(arg1, arg2, arg3)
# 		tracker.print_diff()
# 	return a_wrapper_accepting_arguments


def imgLogic(imgName = None):
	if imgName is None:
		print("Error: please send imgName!")
		return None
	imgPath = 'letters/' + imgName  # path to img
	# print("imgPath", imgPath)
	# img = cv2.imread('letters/a_1.png',0)
	img = cv2.imread(imgPath,0)
	pixels = []
	for n in range(len(img)):
		for m in range(len(img[n])):
			tmp = (255 - int(img[n, m]))/255  # get pixel color val and invert colour (default: white - 255, blk - 0)
			pixels.append(tmp)  # pos n/m check, 
	# print(len(img)*len(img[0]))  # total img pixels ammount
	# print(pixels)
	return pixels


def networkLearningIter(PrevIterNeuralNetwork = None, silent = False, images = None):
	# Network = neuralNetwork.NeuralNetwork([256, 64, 8, 4])  # [256, 64, 4]
	# if 'NetworkList' in locals():
	# 	print("In locals()")
	NetworkList = []
	global numb123
	numb123 += 1 # it counter
	# exactRes = "a"  # 'a', 'b', 'c' or 'd' for extraction
	rightNetworkList = []
	for i in range(8):  # 8 random weight networks

		# from pympler.tracker import SummaryTracker
		# tracker = SummaryTracker()

		

		if PrevIterNeuralNetwork is None:
			# if pixels is not None:
			# 	Network = neuralNetwork.NeuralNetwork([256, 64, 8, 4], pixels, i)  # img and rand weights
			# else:
				Network = neuralNetwork.NeuralNetwork([256, 64, 8, 4], None, i)  # [256, 64, 4]  send img
			# Network.showOutputNeurones()
		else:
				Network = copyObjNetwork(PrevIterNeuralNetwork)
				if i != 0:
					# Network.mutation(0.1, 0.05*i)  # test
					Network.mutation(0.01, 0.1)  # test
				# Network.changeInputVals()

		# all photos send to neural network
		for k in images:
			Network.changeInputVals(k[1])
			calcRes = Network.showChosenLetter(True)
			if calcRes[0] == k[0]:
				# print("Right result =", k[0])
				# print(calcRes, "was giving by N[", i, "]")
				rightNetworkList.append(int(i))
		# Network.correctAmmount()  # fix numeration problem (see neural network's constructor, destructor)
		NetworkList.append(copy.deepcopy(Network))  # try to call manualy __createSynapses()
		NetworkList[len(NetworkList) - 1].initLayers(Network.returnLayers())  # hard copy of neurones Layers

		del Network

	countedList = Counter(rightNetworkList)
	# print("counted rightNetworkList", countedList)  # count list elements
	valsD = countedList.values()
	# print("vals", countedList.values())
	maxValues = max(valsD)
	# print("maxValues", maxValues)

	for key, val in countedList.items():  # return one key of element with max val
		if val == maxValues:
			if key != 0:  # show changing
				print(numb123, " ____________")
				print("network:", key, "detected:", val)
				global preTime1
				print("Iter Time:", time.time() - preTime1)
			bestNeuralNetworkNumber = key
			break

	# tracker.print_diff()

	return copyObjNetwork(NetworkList[bestNeuralNetworkNumber])

	# 	# print(NetworkList[len(NetworkList) - 1].returnLayers())

	# 	calcRes = NetworkList[len(NetworkList) - 1].showChosenLetter(True)
	# 	print(calcRes, len(NetworkList) - 1)
	# 	if calcRes[0] == exactRes:
	# 		# print("Right result!")
	# 		rightNetworkList.append(int(i))

	# # print(NetworkList)
	# if not silent:  # without console output
	# 	print("Right res give this networks:", rightNetworkList)  # +1 because here is real list pos (Network number beginning from 1)
	# 	print("")

	# # choose best res from networks list
	# IterRightNetworks = []
	# IterCalcValRes = []
	# for i in rightNetworkList:
	# 	# print("i",i, "nwtwNumb", NetworkList[i].numb)
	# 	IterRightNetworks.append(copy.deepcopy(NetworkList[i]))  # add right networks to list
	# 	IterRightNetworks[len(IterRightNetworks) - 1].initLayers(NetworkList[i].returnLayers())  # hard copy of neurones Layers
	# 	# del NetworkList[i]


	# 	tempList = NetworkList[i].showChosenLetter(silent)
	# 	IterCalcValRes.append(tempList[1])
	# 	# print("iterationOfCreation:", NetworkList[i].iterationOfCreation)  # debug (one of bug fixes)

	# # print("Best", tempList[0], "is:", max(IterCalcValRes))
	# if len(IterCalcValRes) >= 1:
	# 	maxIterCalcValRes = max(IterCalcValRes)
	# 	# print("Best", "is:", maxIterCalcValRes)
	# 	for i in IterRightNetworks:
	# 		tempRes = i.showChosenLetter(True)
	# 		if tempRes[0] == exactRes and tempRes[1] == maxIterCalcValRes:  # exactRes == a e.x.
	# 			if not silent:  # without console output
	# 				print("Best Network for this iteration:", i)   # the best Network in this iteration
	# 				print("max res for", exactRes, ":", maxIterCalcValRes)
	# 				# i.showChosenLetter()
	# 			# print(i)
	# 			return i
	# else:
	# 	print("networkLearningIter None")
	# 	return None
	# print(IterCalcValRes)


def mutation(bestNeuralNetwork, ammount = 8):  # create weight mutated network
	# mutatedNetworkList = []
	# tmpMutatedNetwork = []

	# print("mutation123", bestNeuralNetwork.mutation())
	# bestNeuralNetwork.showChosenLetter()
	bestNeuralNetwork.mutation()
	# bestNeuralNetwork.showChosenLetter()
	return copyObjNetwork(bestNeuralNetwork)

	# for i in range(ammount):  # 8 mutated weight networks

	# 	mutatedNetworkList.append(copy.deepcopy(bestNeuralNetwork))
	# 	mutatedNetworkList[len(mutatedNetworkList) - 1].initLayers(bestNeuralNetwork.returnLayers())  # hard copy of neurones Layers

		# add func random mutation 
		
		# NetworkList[len(NetworkList) - 1].initLayers(Network.returnLayers())  # hard copy of neurones Layers
		# del Network

def networkLearning(iterationAmmount = 10):
	imgNamesList = ["a_1.png", "a_2.png", "a_3.png", "a_4.png", "a_5.png", \
	"b_1.png", "b_2.png", "b_3.png", "b_4.png", "b_5.png", \
	"c_1.png", "c_2.png", "c_3.png", "c_4.png", "c_5.png", \
	"d_1.png", "d_2.png", "d_3.png", "d_4.png", "d_5.png"]

	# imgNamesList = ["a_1.png", "a_2.png", "b_1.png", "b_2.png", "c_1.png", "c_2.png", "d_1.png", "d_2.png"]  # test

	# imgNamesList = ["a_1.png", "b_1.png", "a_2.png", "b_2.png", "a_3.png", "b_3.png", "a_4.png", "b_4.png", "a_5.png", "b_5.png"]
	images = []
	MutantNetwork = None

	for n in imgNamesList:
		images.append([n[0], imgLogic(n)])
		print(n)

	# for i in imgNamesList:
	# 	pixels = imgLogic(i)
	# 	print(i)

	# 	for n in range(iterationAmmount):
	# 		print("___________________________")
	# 		# res = None
	# 		# del res

	for i in range(iterationAmmount):
		# print(i, "___________________________")

		# print(pixels)
			

		res = None
		while res is None:
			preTime = time.time()
			# print(i[0])
			# res = networkLearningIter(i[0], MutantNetwork, True, pixels)  # get res of iter
			res = networkLearningIter(MutantNetwork, True, images)  # get res of iter
			# print("execution time:", time.time() - preTime)
			# print("res1", res)
			# res.showChosenLetter()

			if res is not None:
				# res.showOutputNeurones()
				MutantNetwork = copyObjNetwork(res)
				# res.showOutputNeurones()
				# print("Mutant:")
				# pixels = imgLogic(i)
				# MutantNetwork = mutation(res)
				# MutantNetwork.showOutputNeurones()
				# MutantNetwork = copyObjNetwork(mutation(res))
				# print("MutantNetwork", MutantNetwork)
				# MutantNetwork.showOutputNeurones()
				# changed = networkLearningIter(i[0], res, True, pixels)  # change img 
				# # changed.changeInputVals("a_2.png")
				# changed.showChosenLetter()
	return res

# make copy of NeuralNetwork obj
def copyObjNetwork(NetworkObjToCopy, delKey = False):
	# print("NetworkObjToCopy", NetworkObjToCopy)
	NetworkCopied = copy.deepcopy(NetworkObjToCopy)
	NetworkCopied.initLayers(NetworkObjToCopy.returnLayers())  # hard copy of neurones Layers
	if delKey:
		del NetworkObjToCopy

	return NetworkCopied



# from pympler.tracker import SummaryTracker
# tracker = SummaryTracker()

# ... some code you want to investigate ...

# networkLearningIter("a", None, False)
# List = networkLearningIter("a", None)
# print("len", len(List))
# List[2].showChosenLetter()
# List[4].showChosenLetter()
# List[2].showChosenLetter()

preTime1 = time.time()
tmp1 = copyObjNetwork(networkLearning(100))

print("++++++++++++++++++++++++++")

# print("a_4.png")
# pixels = imgLogic("a_4.png")
# tmp1.changeInputVals(pixels)
# tmp1.showOutputNeurones()

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

# tracker.print_diff()


# Network.showAllNeurones()  # all neurones showe some info about eachselves

# for i in Network.layers:  # acces to every neurone
# 	for n in i:
# 		n.info()
		# print(n.layer)

# print(Network.layers[1].layer)