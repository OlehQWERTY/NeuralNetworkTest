import math
import random

class Neuron:
	
	genAmmount = 0
	layer = 0
	value = 0  # value 0-1 (only for 1 layer) 
	numb = 0
	synapsesList = None
	weightList = None

	def __init__(self, layer = 0, inputD = 0):
		Neuron.genAmmount += 1
		self.layer = layer
		self.numb = self.howMany(True) # Neuron.genAmmount  # my number among gen neurones
		self.value = inputD
		# print("Hello, I'm ", self.numb)

	def activation(self, x):
		return 1 / (1 + math.exp(-1 * x))

	def synapses(self, neuronesList):  # neuronesList = [[*pointer_1, weight_1], [*pointer_2, weight_2], ...]
		self.synapsesList = neuronesList

		# print("Hello I'm the oldest on this layer!")
		# neuronesList[0].info()
		# print("Len:", len(neuronesList))

		# take a picture data
		# if self.layer == 0:  # init weights with random values
		# 	self.value = 0.11  # change to random (activate???)
		self.weightList = []
		for x in range(len(self.synapsesList)):
			# self.weightList.append( random.uniform(0, 1) )  # random weight
			self.weightList.append( self.activation(random.uniform(0, 1)) )  # random activated weight

		# print(self.synapsesList)
		# print(self.weightList)

	def countValue(self):
		# if self.synapsesList[0] is not None:
		# 	print(self.synapsesList[0].value)
		if self.synapsesList[0] is None:  # layer 0 (because of: self.layers[currentLayer][neuron].synapses( [None] ) in neuralNetwork.py)
		# init weights with random values
			if self.value == 0:  # else image was loaded (no need to init with random)
				self.value = random.uniform(0, 1)  # change to random (activate???)
		else:
			# for neuronInstance in self.synapsesList:
			for neuron in range(len(self.synapsesList)):
				self.value += self.synapsesList[neuron].value * self.weightList[neuron]
				# print("value: ", self.synapsesList[neuron].value)  # why???
		print(self.value)
		self.value = self.activation(self.value)
		# print(self.value)

	@staticmethod
	def howMany(silent = False):
		if not silent:
			print('Neuron\'s ammount {0:d}.'.format(Neuron.genAmmount))
		return Neuron.genAmmount

	def info(self):
		print("Hello, I'm #", self.numb)
		print("come to you from layer #", self.layer)
		print("value:", self.value)
		print("\n")

	# def showValue(self):
	# 	print(self.value)