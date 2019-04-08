# debug is possible to use instead print
from debug import Debug
D = Debug.getInstance()


# telegram notifier
from tCom import TCom as TComImp
TCom = TComImp.getInstance()


# serialize / deserialize obj to/from json
from saveObj import SaveObj  
LogDump = SaveObj("test.dat")


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


# import numpy as np
import cv2
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


def log(*args, **kwargs):
	tmp = ""
	for i in args:
		tmp += str(i) + ' '

	D = Debug.getInstance()
	D.log(tmp)


def logSave():
	LogDump.save(D.getTmpLog())  # create an empty file for dbDataProc.py save


def logRestore():
	D.setTmpLog(LogDump.load())


def logClear():
	D.clearTmpLog()


def getTmpLog(type = "all"):
	return D.getTmpLog(type)


# get list of files in folder
import os 
def ls(directory = None):
	if directory: 
		files = os.listdir(directory)
		return files
	else:
		return None


# memory histogram

# from pympler.tracker import SummaryTracker
# tracker = SummaryTracker()

# funcForTesting()

# tracker.print_diff()

if __name__ == '__main__':  # call only if this module is called independently
	D = Debug.getInstance()
	D.log("1111", [56859, "6lokdjncdj"], {"poiu": "dnkcjdnk"})

	logSave()
	logClear()
	logRestore()
	print(getTmpLog())
