import neuron
import operator  # for max in dict
import copy # try to copy neurones list to fix similar neurones for all NeuralNetwork list objects
import random

class NeuralNetwork:
	genAmmount = 0
	numb = 0
	layersInfo = 0
	layers = []
	imgList = []
	iterationOfCreation = None

	# needs to add copying constructor to fix obj counter error
	def __init__(self, layers, inImgList = None, iterationOfCreation = None):  # iterationOfCreation - test (bugfix idea)
		# print("constructor")
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
		# print("killed")
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

	# not tested
	def changeInputVals(self, inImgList = None):  # only for existing Networks
		# print(len(self.layers), )
		if len(self.layers) == len(self.layersInfo):  # equal sizes means that this network was coppied (innited and with counted data...)
			self.imgList = inImgList  # is changing or stell the same???
			for i in range(self.layersInfo[0]):  # init first layer's val with new img data
				self.layers[0][i].value = self.imgList[i]

			for currentLayer in range(len(self.layersInfo)):
				for neuron in range(len(self.layers[currentLayer])):
					if currentLayer != 0:  # recalc val for all neurones (exept 0 level (they == img data)). Weight leaves the same.
						self.layers[currentLayer][neuron].countValue()
		else:
			print("changeInputVals (NeuralNetwork):", "not appropriate network!")  # copy error msg func (flask prj) or write new decorated one
			return None

	# not tested
	def mutation(self, percentage = 5):  # percentage in range 0 - 100 %
		# self.layersInfo
		# self.layers
		percentage = percentage * 0.01  # convert %
		# print("mutation")

		neuronesAmmount = 1
		for i in self.layersInfo:
			neuronesAmmount *= i
		percentageNeuronesAmmount = int(neuronesAmmount * percentage)

		changing = []
		for i in range(percentageNeuronesAmmount):
			tmpLayerNumb = random.randint(1, (len(self.layersInfo)-1))  # 0 layer has no waight
			tmpNeuroneNumb = random.randint(0, self.layersInfo[tmpLayerNumb] - 1)
			synapsesAmmount = self.layersInfo[tmpLayerNumb - 1]
			tmpSynapse = random.randint(0, synapsesAmmount - 1)
			# print(self.layersInfo[tmpLayerNumb])
			tmpVal = random.uniform(-0.1, 0.1)
			# changing.append([tmpLayerNumb, tmpNeuroneNumb, tmpSynapse,tmpVal])
			# print([tmpLayerNumb, tmpNeuroneNumb, tmpSynapse,tmpVal])
			# # 256, 64, 8, 4
			# print("prev weight", self.layers[tmpLayerNumb][tmpNeuroneNumb].weightList[tmpSynapse])
			self.layers[tmpLayerNumb][tmpNeuroneNumb].weightList[tmpSynapse] = self.layers[tmpLayerNumb][tmpNeuroneNumb].weightList[tmpSynapse] + tmpVal

		for currentLayer in range(len(self.layersInfo)):
			for neuron in range(len(self.layers[currentLayer])):
				self.layers[currentLayer][neuron].countValue()
			# print("mod weight", self.layers[tmpLayerNumb][tmpNeuroneNumb].weightList[tmpSynapse])
		# print("neuronesAmmount", neuronesAmmount)
		# print("neuronesAmmount percentage", percentageNeuronesAmmount)
		# print("weight list", self.layers[1][1].weightList)
		# print("changing", changing)
		# random.randint(12, 56)

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