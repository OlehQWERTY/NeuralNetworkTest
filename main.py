# layer 0: 256, 1: 64, 2: 4

import neuralNetwork

Network = neuralNetwork.NeuralNetwork([256, 64, 4])

for i in Network.layers:
	for n in i:
		n.info()
		# print(n.layer)

# print(Network.layers[1].layer)