# layer 0: 256, 1: 64, 2: 4
import cv2
import numpy as np
import neuralNetwork
# importing "copy" for copy operations 
import copy 

imgNamesList = ["a_1.png", "a_2.png", "a_3.png", "a_4.png", "a_5.png", \
"b_1.png", "b_2.png", "b_3.png", "b_4.png", "b_5.png", \
"c_1.png", "c_2.png", "c_3.png", "c_4.png", "c_5.png", \
"d_1.png", "d_2.png", "d_3.png", "d_4.png", "d_5.png"]

img = cv2.imread('letters/a_1.png',0)
pixels = []
for n in range(len(img)):
	for m in range(len(img[n])):
		tmp = (255 - int(img[n, m]))/255  # get pixel color val and invert colour (default: white - 255, blk - 0)
		pixels.append(tmp)  # pos n/m check, 
# print(len(img)*len(img[0]))  # total img pixels ammount
# print(pixels)
# Network = neuralNetwork.NeuralNetwork([256, 64, 8, 4])  # [256, 64, 4]

NetworkList = []
exactRes = "a"
rightNetworkList = []
for i in range(8):
	Network = neuralNetwork.NeuralNetwork([256, 64, 8, 4], pixels, i)  # [256, 64, 4]  send img
	# Network = neuralNetwork.NeuralNetwork([200, 100, 50, 5], None, i)  # [256, 64, 4]  send img
	# Network.showOutputNeurones()
	calcRes = Network.showChosenLetter()
	if calcRes[0] == exactRes:
		# print("Right result!")
		rightNetworkList.append(int(i))

	NetworkList.append(copy.deepcopy(Network))
	NetworkList[len(NetworkList) - 1].initLayers(Network.returnLayers())  # hard copy of neurones Layers

# print(NetworkList)
print("Right res give this networks:", rightNetworkList)  # +1 because here is real list pos (Network number beginning from 1)

# choose best res from networks list
IterRightNetworks = []
IterCalcValRes = []
for i in rightNetworkList:
	# print("i",i, "nwtwNumb", NetworkList[i].numb)
	IterRightNetworks.append(NetworkList[i])  # add right networks to list
	tempList = NetworkList[i].showChosenLetter()
	IterCalcValRes.append(tempList[1])
	# print("iterationOfCreation:", NetworkList[i].iterationOfCreation)  # ??? wtf

# print(IterCalcValRes)


# IterRightNetworks = 
# for rightNetwork in NetworkList:



# Network.showAllNeurones()  # all neurones showe some info about eachselves

# for i in Network.layers:  # acces to every neurone
# 	for n in i:
# 		n.info()
		# print(n.layer)

# print(Network.layers[1].layer)