# layer 0: 256, 1: 64, 2: 4
import cv2
import numpy as np
import neuralNetwork

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
for i in range(8):
	Network = neuralNetwork.NeuralNetwork([256, 64, 8, 4], pixels)  # [256, 64, 4]  send img
	# Network = neuralNetwork.NeuralNetwork([200, 100, 50, 5])  # [256, 64, 4]  send img
	Network.showOutputNeurones()
	NetworkList.append(Network)

# Network.showAllNeurones()  # all neurones showe some info about eachselves

# for i in Network.layers:  # acces to every neurone
# 	for n in i:
# 		n.info()
		# print(n.layer)

# print(Network.layers[1].layer)