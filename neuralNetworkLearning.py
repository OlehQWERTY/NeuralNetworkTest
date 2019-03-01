# layer 0: 256, 1: 64, 2: 4
import cv2
import numpy as np
import neuralNetwork
import copy  # importing "copy" for copy operations 

tempIterationOOO = 0

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


def networkLearningIter(exactRes, silent = False, pixels = None):
	# Network = neuralNetwork.NeuralNetwork([256, 64, 8, 4])  # [256, 64, 4]
	NetworkList = []
	# exactRes = "a"  # 'a', 'b', 'c' or 'd' for extraction
	rightNetworkList = []
	for i in range(8):
		if pixels is not None:
			Network = neuralNetwork.NeuralNetwork([256, 64, 8, 4], pixels, i)  # [256, 64, 4]  send img
		else:
			Network = neuralNetwork.NeuralNetwork([200, 100, 50, 5], None, i)  # [256, 64, 4]  send img
		# Network.showOutputNeurones()
		calcRes = Network.showChosenLetter(True)
		if calcRes[0] == exactRes:
			# print("Right result!")
			rightNetworkList.append(int(i))

		NetworkList.append(copy.deepcopy(Network))
		NetworkList[len(NetworkList) - 1].initLayers(Network.returnLayers())  # hard copy of neurones Layers

	# print(NetworkList)
	if not silent:  # without console output
		print("Right res give this networks:", rightNetworkList)  # +1 because here is real list pos (Network number beginning from 1)
		print("")

	# choose best res from networks list
	IterRightNetworks = []
	IterCalcValRes = []
	for i in rightNetworkList:
		# print("i",i, "nwtwNumb", NetworkList[i].numb)
		IterRightNetworks.append(NetworkList[i])  # add right networks to list
		tempList = NetworkList[i].showChosenLetter(silent)
		IterCalcValRes.append(tempList[1])
		# print("iterationOfCreation:", NetworkList[i].iterationOfCreation)  # debug (one of bug fixes)

	# print("Best", tempList[0], "is:", max(IterCalcValRes))
	if len(IterCalcValRes) >= 1:
		maxIterCalcValRes = max(IterCalcValRes)
		# print("Best", "is:", maxIterCalcValRes)
		for i in IterRightNetworks:
			tempRes = i.showChosenLetter(True)
			if tempRes[0] == exactRes and tempRes[1] == maxIterCalcValRes:  # exactRes == a e.x.
				if not silent:  # without console output
					print("Best Network for this iteration:", i)   # the best Network in this iteration
					print("max res for", exactRes, ":", maxIterCalcValRes)
					# i.showChosenLetter()
				return i
	else:
		print("networkLearningIter None")
		return None
	# print(IterCalcValRes)


def networkLearning(iterationAmmount = 10, i = None):

	imgNamesList = ["a_1.png", "a_2.png", "a_3.png", "a_4.png", "a_5.png", \
	"b_1.png", "b_2.png", "b_3.png", "b_4.png", "b_5.png", \
	"c_1.png", "c_2.png", "c_3.png", "c_4.png", "c_5.png", \
	"d_1.png", "d_2.png", "d_3.png", "d_4.png", "d_5.png"]

	if i is None:  # if we'll get no result for current iteration repeat it one more time
		for n in range(len(imgNamesList)):
			if i == imgNamesList[n]:
				imgNamesList = imgNamesList[n:-1]  # cut rest of the list with img names
# bug sowhere here --------------------------------------------------------------------------------------------
	for i in imgNamesList:
		pixels = imgLogic(i)
		print(i)

		for n in range(iterationAmmount):
			res = networkLearningIter(i[0], True, pixels)
			if res is None:
				break
		else:
			print("One more networkLearning!")
			networkLearning(iterationAmmount, i)

			# 	n-=1
	# networkLearningIter


networkLearning(1)

# Network.showAllNeurones()  # all neurones showe some info about eachselves

# for i in Network.layers:  # acces to every neurone
# 	for n in i:
# 		n.info()
		# print(n.layer)

# print(Network.layers[1].layer)