# from debug import debug

# log = debug(True)

# log.log("koko")

# log(self.WARNING + name) or log.log(log.WARNING + name) from outside

import functools
import sys
import os
import inspect


# def _debugDecorator(function_to_decorate):
#     @functools.wraps(function_to_decorate)
#     def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
#     # def a_wrapper_accepting_arbitrary_arguments(self, s, name):
#         # print("Передали ли мне что-нибудь?:")
#         # print(args)
#         # print(kwargs)

#         function_to_decorate(*args, **kwargs)
#     return a_wrapper_accepting_arbitrary_arguments

class Debug:
    # colours for messages
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ORDINARY = '\033[0m'

    def __init__(self, flag, name=None):
        # print(sys._getframe().f_code.co_name)
        if flag:
            # if name is not None:
            #    print(name, "module turn on debugging")
            self.DEBUG = True
        else:
            self.DEBUG = False

    # @_debugDecorator
    def log(self, *args, **kwargs):
        name = "__main__"
    # def log(self, s, name=None):
        if self.DEBUG:  # DEBUG = True
            try:
                if name is None:  # analog for ordinary print func
                    # print(s)
                    print("args")
                else:
                    if name == "__main__":  # other colour for __main__
                        # print(args, **kwargs)
                        # print(self.OKBLUE + name + ": " + self.ORDINARY, s)
                        tmp = ""
                        for i in args:
                            tmp += i + ' '

                        print(self.OKBLUE + name + ":" + self.ORDINARY, tmp[:-1])
                        print(sys._getframe(1).f_code.co_name)
                        print(sys._getframe().f_code.co_name)
                        # print(__file__)
                        print(os.path.basename(__file__))
                        print(os.path.realpath(__file__))
                        print(inspect.getfile(inspect.currentframe()))         # lib/bar.py



                        frame = inspect.stack()[1]
                        module = inspect.getmodule(frame[0])
                        # module = sys._getframe(1).f_code.co_name
                        print("module.__file__", module.__file__)  # finaly)))

                    # else:
                        # print(self.WARNING + name + ": " + self.ORDINARY + s)  #  + name, ": " (space b name & :)
                        # print(self.WARNING + name + ": " + self.ORDINARY + s)  #  + name, ": " (space b name & :)
                    return self.DEBUG
            except TypeError:  # not possible to convert to str() (e.x. [list])
               # do something with None here
                print(self.WARNING + name + ": ", self.ORDINARY, s)
            except ValueError:
                print(self.FAIL + name + ": " + self.ORDINARY + "ValueError")








# if __name__ == "__main__":

#     d = Debug(True)

#     # d.log(d.WARNING + "Lolo", "KO")
#     d.log("lololo", "kjdf")

