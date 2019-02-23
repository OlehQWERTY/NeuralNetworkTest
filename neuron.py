import math

class Neuron:
	
	genAmmount = 0
	layer = 0
	value = 0  # value 0-1 (only for 1 layer) 
	numb = 0

	def __init__(self, layer = 0, input = 0):
		Neuron.genAmmount += 1
		self.layer = layer
		self.numb = self.howMany(True) # Neuron.genAmmount  # my number among gen neurons
		# print("Hello, I'm ", self.numb)

	def activation(self, x):
		return 1 / (1 + math.exp(-1 * x))

	@staticmethod
	def howMany(silent = False):
		print(silent)
		if not silent:
			print('Neuron\'s ammount {0:d}.'.format(Neuron.genAmmount))
		
		return Neuron.genAmmount

	def info(self):
		print("Hello, I'm #", self.numb)
		print("come to you from layer #", self.layer)
		print("\n")