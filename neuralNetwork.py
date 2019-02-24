import neuron

class NeuralNetwork:
	# layersAmmount = 0
	layersInfo = 0
	layers = []

	def __init__(self, layers):
		# self.layersAmmount = len(layers)
		self.layersInfo = layers
		print("Network: ", self.layersInfo, "\n")

		for x in self.layersInfo:
			self.__createLayer(x)

		self.__createSynapses()

	def __createLayer(self, layerSize):
		arrLayer = []
		for i in range(layerSize):  # create all neurones for layer
			arrLayer.append(neuron.Neuron(len(self.layers)))  # leyer's number beginning from 0

		self.layers.append(arrLayer)  # add layer

	def __createSynapses(self):
		# currentLayer = 0
		
		# if currentLayer > 0:
		# 	self.layers[currentLayer][0].synapses( self.layers[currentLayer - 1] )  # send all previous layer to neurone

		# print(self.layers[currentLayer - 1])
		for currentLayer in range(len(self.layersInfo)):
			# print(currentLayer)
			
			for neuron in range(len(self.layers[currentLayer])):
				if currentLayer == 0:
					self.layers[currentLayer][neuron].synapses( [None] )  # first layer
				else:
					self.layers[currentLayer][neuron].synapses( self.layers[currentLayer - 1] )  # currentLayer - 1 - prelayer

				self.layers[currentLayer][neuron].countValue()
			# print(neuron)
		
		# self.layers[currentLayer][0].info()  # neurone for synapse func()

	def showAllNeurones(self):
		for n in self.layers:
			for m in n:
				m.info()

# N = neuron.Neuron()
# N1 = neuron.Neuron()
# N2 = neuron.Neuron()
# N2.howMany()
# N2.howMany()

# print(N2.activation(8))
# print("main")