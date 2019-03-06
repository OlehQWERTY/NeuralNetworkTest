import math
import random

class Neuron:
	
	genAmmount = 0
	layer = 0
	value = -1  # value 0-1 is taken from an img (if exist)
	numb = 0
	synapsesList = None
	weightList = None
	iterationOfCreation = None  # test for bugfix

	def __init__(self, layer = 0, inputD = 0, iterationOfCreation = None):
		Neuron.genAmmount += 1
		self.layer = layer
		self.numb = self.howMany(True) # Neuron.genAmmount  # my number among gen neurones
		self.value = inputD
		self.iterationOfCreation = iterationOfCreation

	def activation(self, x):
		return 1 / (1 + math.exp(-1 * x))

	def synapses(self, neuronesList):  # neuronesList = [[*pointer_1, weight_1], [*pointer_2, weight_2], ...]
		self.synapsesList = neuronesList
		self.weightList = []

		if self.synapsesList[0] is not None:  # layer 0 (because of: self.layers[currentLayer][neuron].synapses( [None] ) in neuralNetwork.py)
			for x in range(len(self.synapsesList)):
				self.weightList.append( random.uniform(-1, 1) )  # random weight
				# self.weightList.append( self.activation(random.uniform(0, 1)) )  # random activated weight (-1, 1) to solve neuron value > 1 

	def countValue(self):
		if self.synapsesList[0] is None and self.layer == 0:  # layer 0 (because of: self.layers[currentLayer][neuron].synapses( [None] ) in neuralNetwork.py)
		# init weights with random values
			if self.value == -1:  # else image was loaded (no need to init with random)
				self.value = random.uniform(0, 1)  # not activated
		else:  # any layer exept 0 layer
			self.value = 0  # default val == -1
			for neuron in range(len(self.synapsesList)):
				# print(self.synapsesList[neuron].value * self.weightList[neuron])
				self.value += self.synapsesList[neuron].value * self.weightList[neuron]
		self.value = self.activation(self.value)

	@staticmethod
	def howMany(silent = False):
		if not silent:
			print('Neuron\'s ammount {0:d}.'.format(Neuron.genAmmount))
		return Neuron.genAmmount

	def info(self):
		print("Hello, I'm #", self.numb)
		print("come to you from layer #", self.layer)
		print("value[", self.numb, ']:', self.value)
		print("\n")