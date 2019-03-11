# usage:
# s = Singleton()
# print(s)

# s = Singleton.getInstance()
# print(s)

import os

# singleton
class Singleton:
	__instance = None
	__linesList = []
	@staticmethod 
	def getInstance():
		""" Static access method. """
		if Singleton.__instance == None:
			Singleton()
		return Singleton.__instance
	def __init__(self):
		""" Virtually private constructor. """
		if Singleton.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			Singleton.__instance = self


	def addLine(self, str):
		Singleton.__linesList.append(str)

	def show(self, shift = False):
		if shift:
			for i in range(20):
				print("")
				
		os.system("clear")
		for line in Singleton.__linesList:
			print(line)

	def clearLines(self, numb):
		if isinstance(numb, int):
			del Singleton.__linesList[numb]
		else:
			for i in numb:
				del Singleton.__linesList[i]

	def indexOf(self, tmpStr):
		return Singleton.__linesList.index(tmpStr)



