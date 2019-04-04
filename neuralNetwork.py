import neuron
import operator  # for max in dict
import copy
import random
import sys
sys.path.append('./utility')
from utility import Debug
D = Debug.getInstance()  # get debug obj


class NeuralNetwork:
	genAmmount = 0
	numb = 0
	layersInfo = 0
	layers = []
	imgList = []
	iterationOfCreation = None

	# needs to add copying constructor to fix obj counter error
	def __init__(self, layers, inImgList = None, iterationOfCreation = None):  # iterationOfCreation - test (bugfix idea)
		NeuralNetwork.genAmmount += 1  
		self.numb = self.howMany(True) # Neuron.genAmmount  # my number among gen neurones
		self.layersInfo = layers
		self.imgList = inImgList
		self.iterationOfCreation = iterationOfCreation  # test (bug fix)

		for x in range(len(self.layersInfo)):
			flag = False
			if x == 0 and self.imgList is not None and len(self.imgList) == self.layersInfo[0]:
				flag = True
			self.__createLayer(self.layersInfo[x], flag)

		self.__createSynapses()

	def __del__(self):  # ammount -1 (problem with coppied objsects)
		NeuralNetwork.genAmmount -= 1
		self.release_list(self.layers)

	def release_list(self, a):  # fixes memory leakage
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

	def changeInputVals(self, inImgList = None):  # only for existing Networks
		if len(self.layers) == len(self.layersInfo):  # equal sizes means that this network was coppied (innited and with counted data...)
			self.imgList = inImgList  # is changing or stell the same???
			for i in range(self.layersInfo[0]):  # init first layer's val with new img data
				self.layers[0][i].value = self.imgList[i]

			for currentLayer in range(len(self.layersInfo)):
				for neuron in range(len(self.layers[currentLayer])):
					if currentLayer != 0:  # recalc val for all neurones (exept 0 level (they == img data)). Weight leaves the same.
						self.layers[currentLayer][neuron].countValue()
		else:
			D.log("changeInputVals (NeuralNetwork):", "not appropriate network!")  # copy error msg func (flask prj) or write new decorated one
			return None

	def mutation(self, percentage = 0.01, val = 0.01):  # percentage in range 0 - 100 %
		percentage = percentage * 0.01  # convert %

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
			tmpVal = random.uniform(-1*val, val)  # -0.2, 0.2
			candidateNewWeight = self.layers[tmpLayerNumb][tmpNeuroneNumb].weightList[tmpSynapse] + tmpVal
			if candidateNewWeight < 1 and candidateNewWeight > -1:
				self.layers[tmpLayerNumb][tmpNeuroneNumb].weightList[tmpSynapse] = self.layers[tmpLayerNumb][tmpNeuroneNumb].weightList[tmpSynapse] + tmpVal
			else:
				# no changes
				pass;

		for currentLayer in range(len(self.layersInfo)):
			for neuron in range(len(self.layers[currentLayer])):
				self.layers[currentLayer][neuron].countValue()

	def showAllNeurones(self):
		for n in self.layers:
			for m in n:
				m.info()

	def showOutputNeurones(self):
		for neuronInstance in self.layers[len(self.layersInfo) - 1]:  # show last layer
			# neuronInstance.info()
			neuronInstance.shortInfo()

	def showChosenLetter(self, silent = True):
		# temp to show a, b, c, d
		lettersArr = ["a", "b", "c", "d"]
		tempArr = {"a": 0, "b": 0, "c": 0, "d": 0}
		for neuron in range(4): 
			tempArr[lettersArr[neuron]] = self.layers[len(self.layersInfo) - 1][neuron].value
		theBiggestValKey = max(tempArr.items(), key=operator.itemgetter(1))[0]
		maxKeyAndVal = [theBiggestValKey, tempArr[theBiggestValKey]]
		if not silent:
			D.log("Res[", self.numb, "]:", maxKeyAndVal)
		return(maxKeyAndVal)

	def outputResQuality(self, expectedRes):
		suma = 0
		lettersArr = ["a", "b", "c", "d"]
		tempArr = {"a": 0, "b": 0, "c": 0, "d": 0}
		for neuron in range(4): 
			tempArr[lettersArr[neuron]] = self.layers[len(self.layersInfo) - 1][neuron].value
			suma += self.layers[len(self.layersInfo) - 1][neuron].value  # sum of all values (a, b, c, d)
		return tempArr[expectedRes]/suma
		# D.log(tempArr)

	def returnLayers(self):
		return copy.deepcopy(self.layers)

	def initLayers(self, layers):
		self.layers = copy.deepcopy(layers)
			
	@staticmethod
	def howMany(silent = False):
		if not silent:
			D.log('NeuralNetwork\'s ammount {0:d}.'.format(NeuralNetwork.genAmmount))
		return NeuralNetwork.genAmmount