# layer 0: 256, 1: 64, 2: 4
import cv2
import numpy as np
import neuralNetwork

img = cv2.imread('letters/a_1.png',0)
# pixel = int(img[8, 5])
# print(pixel)
pixels = []
for n in range(len(img)):
	for m in range(len(img[n])):
		tmp = int(img[n, m])
		if tmp == 0:
			tmp = 1  # fix 0 is not innited (in neuron.py)
		pixels.append(int(img[n, m]))  # pos n/m check, white - 255, blk - 0
# pixeles.append()
# print(len(img)*len(img[0]))
# print(pixels)
# Network = neuralNetwork.NeuralNetwork([256, 64, 8, 4])  # [256, 64, 4]
Network = neuralNetwork.NeuralNetwork([256, 64, 8, 4], pixels)  # [256, 64, 4]  send img

# Network.showAllNeurones()  # all neurones showe some info about eachselves

for i in Network.layers:  # acces to every neurone
	for n in i:
		n.info()
		# print(n.layer)

# print(Network.layers[1].layer)