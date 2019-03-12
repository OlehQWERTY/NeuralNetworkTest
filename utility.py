from debug import Debug

def toFixed(numObj, digits=0):  # ammount of signs after .
    return f"{numObj:.{digits}f}"


# max or min element's index of the list
def extrameListVal(values, isMinLevel = False):
	if isMinLevel:
		return values.index(min(values))
	else:
		return values.index(max(values))


# make copy of NeuralNetwork obj
import copy  # importing "copy" for copy operations 
def copyObjNetwork(NetworkObjToCopy, delKey = False):
	NetworkCopied = copy.deepcopy(NetworkObjToCopy)
	NetworkCopied.initLayers(NetworkObjToCopy.returnLayers())  # hard copy of neurones Layers
	if delKey:
		del NetworkObjToCopy

	return NetworkCopied


import cv2
# import numpy as np
def imgLogic(imgName = None):
	if imgName is None:
		print("Error: please send imgName!")
		return None
	imgPath = 'letters/' + imgName  # path to img
	img = cv2.imread(imgPath,0)
	pixels = []
	for n in range(len(img)):
		for m in range(len(img[n])):
			tmp = (255 - int(img[n, m]))/255  # get pixel color val and invert colour (default: white - 255, blk - 0)
			pixels.append(tmp)  # pos n/m check, 
	# print(len(img)*len(img[0]))  # total img pixels ammount
	# print(pixels)
	return pixels


# write normal Singleton, debug class and so on...


# make it possible to use with different params ammount
# def a_decorator_debug(function_to_decorate):
# 	def a_wrapper_accepting_arguments(arg1, arg2, arg3):
# 		from pympler.tracker import SummaryTracker
# 		tracker = SummaryTracker()
# 		# print("See what I got:", arg1, arg2, arg3)
# 		function_to_decorate(arg1, arg2, arg3)
# 		tracker.print_diff()
# 	return a_wrapper_accepting_arguments










# d = Debug(True)

# # d.log(d.WARNING + "Lolo", "KO")
# d.log("lololo", "kjdf")