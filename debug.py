import inspect  # required to get caller script file's name
import time
import datetime

class Debug:
    # colours for messages
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
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
    WARNING = '\033[93m'
    # Don't work on Windows
    ENDC = '\033[0m'  
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    ORDINARY = '\033[0m'

    colorsList = [  # available for auto coloring
        ["HEADER", '\033[95m'],
        ["OKBLUE", '\033[94m'],
        ["OKGREEN", '\033[92m'],
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
    fSILENT = False
    whoCalledFileNameList = []
    newFileNumb = 1
    logData = {"error": [], \
        "critical_error": [], \
        "sys": [], \
        "warning": [], \
        "msg": []}

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

        timestr = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}"
        self.tmpLog("sys", whoCalledFileName + "[" + timestr + "]:", "Debugging is turned ON by constructor!")
        print(self.FAIL + whoCalledFileName + "[" + timestr + "]:", "Debugging is turned ON by constructor!" + self.ORDINARY)
 

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
                    timestr = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}"
                    self.tmpLog("msg", whoCalledFileName  + "[" + timestr + "]: " + tmp[:-1])
                    if not self.fSILENT:
                        print(self.colorIndex(whoCalledFileName) + whoCalledFileName  + "[" + timestr + "]:" + self.ORDINARY, tmp[:-1])
                return self.fDEBUG
            except TypeError:  # not possible to convert to str() (e.x. [list])
                timestr = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}"
                self.tmpLog("error", whoCalledFileName + "[" + timestr + "]:" + "ValueTypeError")

                if not self.fSILENT:                    
                    print(self.FAIL + whoCalledFileName + "[" + timestr + "]:" + self.ORDINARY + "ValueTypeError")
            except ValueError:
                timestr = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}"
                self.tmpLog("error", whoCalledFileName + "[" + timestr + "]:" + "ValueError")

                if not self.fSILENT:
                    print(self.FAIL + whoCalledFileName + "[" + timestr + "]:" + self.ORDINARY + "ValueError")


    def colorIndex(self, whoCalledFileName):  # different color for different files
        for i in self.whoCalledFileNameList:
            if i[1] == whoCalledFileName:
                return self.colorsList[i[0]][1]


    def turnON_OFF(self, flg = True, silent = False):
        #  not possible to make func from it (return folder of this func)
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        tmpWhoCalledFileName = module.__file__  # file name of whoCalled me e.x. neuralNetworkLearning.py
        whoCalledFileName_TMP = tmpWhoCalledFileName.split('\\')
        whoCalledFileName = whoCalledFileName_TMP[-1]

        timestr = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}"
        if flg == True:
            if silent == True:
                self.tmpLog("sys", whoCalledFileName + "[" + timestr + "]:", "Debugging is turned ON in silent mode!")
                print(self.FAIL + whoCalledFileName + "[" + timestr + "]:", "Debugging is turned ON in silent mode!" + self.ORDINARY)
            else:
                self.tmpLog("sys", whoCalledFileName + "[" + timestr + "]:", "Debugging is turned ON in normal mode!")
                print(self.FAIL + whoCalledFileName + "[" + timestr + "]:", "Debugging is turned ON in normal mode!" + self.ORDINARY)
            self.fSILENT = silent
        else:
            self.tmpLog("sys", whoCalledFileName + "[" + timestr + "]:", "Debugging is turned OFF!")
            print(self.FAIL + whoCalledFileName + "[" + timestr + "]:", "Debugging is turned OFF!" + self.ORDINARY)
        self.fDEBUG = flg


    #  log data storage
    def tmpLog(self, type = "msg", *args, **kwargs):  # type error, critical_error, warning, msg
        tmp = ""
        for i in args:
            tmp += str(i) + ' '

        if type == "error":
            self.logData["error"].append(tmp)
        elif type == "critical_error":
            self.logData["critical_error"].append(tmp)
        elif type == "warning":
            self.logData["warning"].append(tmp)
        elif type == "sys":
            self.logData["sys"].append(tmp)
        if type == "msg":
            self.logData["msg"].append(tmp)


    #  if it is needed save it whenever
    def getTmpLog(self, type = "all"):  # type error, warning, msg, all
        if self.logData:
            if type == "all":
                return self.logData.copy()  # return dict
            elif type == "error":
                return self.logData["error"].copy()  # return list
            elif type == "critical_error":
                return self.logData["critical_error"].copy()  # return list
            elif type == "warning":
                return self.logData["warning"].copy()  # return list
            elif type == "sys":
                return self.logData["sys"].copy()  # return list
            elif type == "msg":
                return self.logData["msg"].copy()  # return list
            else:
                # error not correct log type
                return None
        else:
            return None


    def setTmpLog(self, outLogData):  # load somwhere out, give it here
        #  not possible to make func from it (return folder of this func)
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        tmpWhoCalledFileName = module.__file__  # file name of whoCalled me e.x. neuralNetworkLearning.py
        whoCalledFileName_TMP = tmpWhoCalledFileName.split('\\')
        whoCalledFileName = whoCalledFileName_TMP[-1]

        timestr = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}"
        self.logData = logData.copy()  # it is possible to load data in any fDEBUG state
        if self.fDEBUG == True:
            self.tmpLog("sys", whoCalledFileName + "[" + timestr + "]:", "TmpLog was set!")

            if self.fSILENT == False:
                print(self.FAIL + whoCalledFileName + "[" + timestr + "]:", "TmpLog was set!" + self.ORDINARY)


    def showTmpLog(self):
        pass  # display it coloured


    #  clear after saving, manualy because it is possible to fault with saving
    def clearTmpLog(self):
        for key in self.logData.keys():
            # print(self.logData[key])
            self.logData[key].clear()

if __name__ == "__main__":

    D = Debug.getInstance()
    D.log("lolo", "jdjdnc", "12354")

    d = Debug.getInstance()
    d.log("koko", "lol")

    # D.turnON_OFF(False)  # turn OFF (default is ON)
    # D.turnON_OFF(True, True)  # turn ON in silent mode
    # D.turnON_OFF(True, False)  # turn ON in normal mode

    # print("getTmpLog:")
    # print(d.getTmpLog())
    # D.clearTmpLog()
    d.log("58975", [12, "lo"], {"key": "val"})

    print("getTmpLog:")
    test1 = d.getTmpLog()
    print(test1)

    print("clearTmpLog:")
    D.clearTmpLog()
    # print("getTmpLog:")
    # print(d.getTmpLog())

    # print("setTmpLog:")
    # D.setTmpLog(test1)
    print("getTmpLog:")
    print(d.getTmpLog())


    # print(D.getTmpLog())

    # print(D.FAIL, D.getTmpLog("sys"), D.ORDINARY)


    

