import neuron
import operator  # for max in dict
import copy # try to copy neurones list to fix similar neurones for all NeuralNetwork list objects

class NeuralNetwork:
	genAmmount = 0
	numb = 0
	layersInfo = 0
	layers = []
	imgList = []
	iterationOfCreation = None

	def __init__(self, layers, inImgList = None, iterationOfCreation = None):  # iterationOfCreation - test (bugfix idea)
		print("constructor")
		NeuralNetwork.genAmmount += 1
		self.numb = self.howMany(True) # Neuron.genAmmount  # my number among gen neurones
		# self.layersAmmount = len(layers)
		self.layersInfo = layers
		self.imgList = inImgList
		self.iterationOfCreation = iterationOfCreation  # test (bug fix)
		# print("Network [", self.numb, "]:", self.layersInfo, "\n")

		for x in range(len(self.layersInfo)):
			flag = False
			if x == 0 and self.imgList is not None and len(self.imgList) == self.layersInfo[0]:
				flag = True
			self.__createLayer(self.layersInfo[x], flag)

		self.__createSynapses()

	def __del__(self):  # ammount -1 (problem with coppied objsects)
		NeuralNetwork.genAmmount -= 1
		print("killed")
		self.release_list(self.layers)

	def release_list(self, a):  # try to fix memory leakage
		del a[:]
		del a

	def __createLayer(self, layerSize, flag = False):  # flag - create 0 layer with img values 
		arrLayer = []
		for i in range(layerSize):  # create all neurones for layer
			if flag == True:
				arrLayer.append(neuron.Neuron(len(self.layers), self.imgList[i], self.iterationOfCreation))  # load img to 0 layer
			else:
				arrLayer.append(neuron.Neuron(len(self.layers), 0, self.iterationOfCreation))  # leyer's number beginning from 0
		self.layers.append(arrLayer)  # add layer

	def __createSynapses(self):
		for currentLayer in range(len(self.layersInfo)):
			for neuron in range(len(self.layers[currentLayer])):
				if currentLayer == 0:
					self.layers[currentLayer][neuron].synapses( [None] )  # first layer
				else:
					self.layers[currentLayer][neuron].synapses( self.layers[currentLayer - 1] )  # currentLayer - 1 - prelayer

				self.layers[currentLayer][neuron].countValue()

	def showAllNeurones(self):
		for n in self.layers:
			for m in n:
				m.info()

	def showOutputNeurones(self):
		for neuronInstance in self.layers[len(self.layersInfo) - 1]:  # show last layer
			neuronInstance.info()

	def showChosenLetter(self, silent = False):
		# temp to show a, b, c, d
		lettersArr = ["a", "b", "c", "d"]
		tempArr = {"a": 0, "b": 0, "c": 0, "d": 0}
		for neuron in range(4): 
			# print("layers")  # test
			# print(self.layers)  # test
			tempArr[lettersArr[neuron]] = self.layers[len(self.layersInfo) - 1][neuron].value
		theBiggestValKey = max(tempArr.items(), key=operator.itemgetter(1))[0]
		maxKeyAndVal = [theBiggestValKey, tempArr[theBiggestValKey]]
		if not silent:
			print("Res[", self.numb, "]:", maxKeyAndVal)
		return(maxKeyAndVal)

	def returnLayers(self):
		# print("returnLayers", self.layers)
		return copy.deepcopy(self.layers)  # list copy ???

	def initLayers(self, layers):
		self.layers = copy.deepcopy(layers)  # deep.copy try
		# print("Init")
		# print(layers)
			
	@staticmethod
	def howMany(silent = False):
		if not silent:
			print('NeuralNetwork\'s ammount {0:d}.'.format(NeuralNetwork.genAmmount))
		return NeuralNetwork.genAmmount