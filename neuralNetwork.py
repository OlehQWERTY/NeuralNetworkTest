import neuron

class NeuralNetwork:
	# layersAmmount = 0
	layersInfo = 0
	layers = []

	def __init__(self, layers):
		# self.layersAmmount = len(layers)
		self.layersInfo = layers
		print("Network: ", self.layersInfo)

		for x in self.layersInfo:
			self.__createLayer(x)

	def __createLayer(self, layerSize):
		arrLayer = []
		for i in range(layerSize):  # create all neurones for layer
			arrLayer.append(neuron.Neuron(len(self.layers) + 1))

		self.layers.append(arrLayer)  # add layer

# N = neuron.Neuron()
# N1 = neuron.Neuron()
# N2 = neuron.Neuron()
# N2.howMany()
# N2.howMany()

# print(N2.activation(8))
# print("main")