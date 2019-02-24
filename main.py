# layer 0: 256, 1: 64, 2: 4

import neuralNetwork

Network = neuralNetwork.NeuralNetwork([4, 2, 1])  # [256, 64, 4]

# Network.showAllNeurones()  # all neurones showe some info about eachselves

for i in Network.layers:  # acces to every neurone
	for n in i:
		n.info()
		# print(n.layer)

# print(Network.layers[1].layer)