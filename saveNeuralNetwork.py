import sys, os
import pickle  # serializer/deserializer
from utility import Debug
# sys.path.append('../models')
D = Debug.getInstance()
D.log("___ TEST FOR BEST NETWORK! ___")

class Settings():
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

    # def parse(self):
    #     if self.data_new is not None:
    #         pass

    # def __del__(self):
    #     D.log("Settings is closed!")
    #     sleep(2)


if __name__ == '__main__':  # call only if this module is called independently
    Set = Settings("test.dat")

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


