import sys, os
import pickle  # serializer/deserializer
from debug import Debug  # if utility import - crossing links with utility.py
# sys.path.append('../models')
D = Debug.getInstance()

class SaveObj():
    def __init__(self, path):
        self.path = path
        self.data_new = None
        self.data = None

    def setPath(self, path):
        self.path = path

    def load(self):
        if self.path is not None:
            if not os.path.exists(self.path):
                print(self.path)
                D.log("Can't load file, because it doesn't exist!")
        else:
            D.log("Path is empty!")

        with open(self.path, 'rb') as f:
            self.data_new = pickle.load(f)
            return self.data_new

        return None

    def save(self, data):
        self.data = data
        with open(self.path, 'wb') as f:
            pickle.dump(data, f)
        D.log("Object was saved successfully...")



if __name__ == '__main__':  # call only if this module is called independently
    Set = SaveObj("testSaveObj.dat")

    # data = {
    #     'cam': [0, 640, 480],
    #     'soleImgPos': [45, 169, 594, 360],
    #     'auto': True,
    #     'imgSave': False,
    #     'autoImgQR': False
    # }

    # Set.save(data)
    Set.save([])  # create an empty file for dbDataProc.py save
    print(Set.load())


