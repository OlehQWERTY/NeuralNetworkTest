from debug import Debug
from saveObj import SaveObj  # serialize / deserialize obj to/from json

# ammount of signs after .
def toFixed(numObj, digits=0):
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

# memory histogram

# from pympler.tracker import SummaryTracker
# tracker = SummaryTracker()

# funcForTesting()

# tracker.print_diff()