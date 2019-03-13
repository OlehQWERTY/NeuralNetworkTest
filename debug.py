#  from debug import Debug

#  class is singleton!!!

#  D = Debug.getInstance(True)

#  D.log("lolo", "jdjdnc", "12354")

#  D.turnON_OFF(False)  # turn OFF

import inspect  # required to get caller script file's name

class Debug:
    # colours for messages
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    LIGHTGREY = '\033[37m'
    DARKGREY = '\033[90m'
    LIGHTRED = '\033[91m'
    LIGHTGREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHTBLUE = '\033[94m'
    PINK = '\033[95m'
    LIGHTCYAN = '\033[96m'
    # reserved for error and sys msg only
    FAIL = '\033[91m'
    # Don't work on Windows
    ENDC = '\033[0m'  
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    ORDINARY = '\033[0m'

    colorsList = [  # available for auto coloring
        ["HEADER", '\033[95m'],
        ["OKBLUE", '\033[94m'],
        ["OKGREEN", '\033[92m'],
        ["WARNING", '\033[93m'],
        ["ORANGE", '\033[33m'],
        ["BLUE", '\033[34m'],
        ["PURPLE", '\033[35m'],
        ["CYAN", '\033[36m'],
        ["LIGHTGREY", '\033[37m'],
        ["DARKGREY", '\033[90m'],
        ["LIGHTRED", '\033[91m'],
        ["LIGHTGREEN", '\033[92m'],
        ["YELLOW", '\033[93m'],
        ["LIGHTBLUE", '\033[94m'],
        ["PINK", '\033[95m'],
        ["LIGHTCYAN", '\033[96m']
    ]

    fDEBUG = True
    whoCalledFileNameList = []
    newFileNumb = 1

    __instance = None
    __linesList = []
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Debug.__instance == None:
            Debug()
        return Debug.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if Debug.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Debug.__instance = self
        #  not possible to make func from it (return folder of this func)
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        tmpWhoCalledFileName = module.__file__  # file name of whoCalled me e.x. neuralNetworkLearning.py
        whoCalledFileName_TMP = tmpWhoCalledFileName.split('\\')
        whoCalledFileName = whoCalledFileName_TMP[-1]

        print(self.FAIL + whoCalledFileName + ":", "Debugging is turned ON by constructor!", self.ORDINARY)
 

    def log(self, *args, **kwargs):
        if self.fDEBUG:  # DEBUG = True
            try:
                #  not possible to make func from it (return folder of this func)
                frame = inspect.stack()[1]
                module = inspect.getmodule(frame[0])
                tmpWhoCalledFileName = module.__file__  # file name of whoCalled me e.x. neuralNetworkLearning.py
                whoCalledFileName_TMP = tmpWhoCalledFileName.split('\\')
                whoCalledFileName = whoCalledFileName_TMP[-1]

                if whoCalledFileName:  # other colour for __main__
                    if whoCalledFileName not in self.whoCalledFileNameList:
                        self.whoCalledFileNameList.append([self.newFileNumb % len(self.colorsList), whoCalledFileName])
                        self.newFileNumb += 1

                    tmp = ""
                    for i in args:
                        tmp += str(i) + ' '

                    # print(self.OKBLUE + whoCalledFileName + ":" + self.ORDINARY, tmp[:-1])
                    print(self.colorIndex(whoCalledFileName) + whoCalledFileName + ":" + self.ORDINARY, tmp[:-1])
                return self.fDEBUG
            except TypeError:  # not possible to convert to str() (e.x. [list])
               # do something with None here 
                tmp = ""
                for i in args:
                    tmp += i + ' '
                print(self.colorIndex(whoCalledFileName) + whoCalledFileName + ":", self.ORDINARY, tmp[:-1])
            except ValueError:
                print(self.FAIL + whoCalledFileName + ":" + self.ORDINARY + "ValueError")

    def colorIndex(self, whoCalledFileName):
        for i in self.whoCalledFileNameList:
            if i[1] == whoCalledFileName:
                return self.colorsList[i[0]][1]

    def turnON_OFF(self, flg = True):
        #  not possible to make func from it (return folder of this func)
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        tmpWhoCalledFileName = module.__file__  # file name of whoCalled me e.x. neuralNetworkLearning.py
        whoCalledFileName_TMP = tmpWhoCalledFileName.split('\\')
        whoCalledFileName = whoCalledFileName_TMP[-1]
        if flg == True:
            print(self.FAIL + whoCalledFileName + ":", "Debugging is turned ON!", self.ORDINARY)
        else:
            print(self.FAIL + whoCalledFileName + ":", "Debugging is turned OFF!", self.ORDINARY)
        self.fDEBUG = flg

if __name__ == "__main__":

    D = Debug.getInstance()
    D.log("lolo", "jdjdnc", "12354")

    d = Debug.getInstance()
    d.log("koko", "lol")

    # D.turnON_OFF(False)  # turn OFF (default is ON)
    # D.turnON_OFF(True)  # turn ON

