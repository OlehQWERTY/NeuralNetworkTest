import neuron

class NeuralNetwork:
	# layersAmmount = 0
	layersInfo = 0
	layers = []
	imgList = []

	def __init__(self, layers, inImgList = None):
		# self.layersAmmount = len(layers)
		self.layersInfo = layers
		self.imgList = inImgList
		print("Network: ", self.layersInfo, "\n")

		for x in range(len(self.layersInfo)):
			flag = False
			if x == 0 and self.imgList is not None and len(self.imgList) == self.layersInfo[0]:
				flag = True
			self.__createLayer(self.layersInfo[x])

		self.__createSynapses()

	def __createLayer(self, layerSize, flag = False):
		arrLayer = []
		for i in range(layerSize):  # create all neurones for layer
			if flag == True:
				arrLayer.append(neuron.Neuron(len(self.layers), self.imgList[i]))  # load img to 0 layer
				print("suka", self.imgList[i])
			else:
				arrLayer.append(neuron.Neuron(len(self.layers)))  # leyer's number beginning from 0
		# print(self.imgList)
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