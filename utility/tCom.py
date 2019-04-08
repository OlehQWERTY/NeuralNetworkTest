# -*- coding: utf-8 -*-

# telegram notifier

import datetime

class TCom:
# class is a singleton

    __instance = None
    __linesList = []


    @staticmethod 
    def getInstance():
        """ Static access method. """
        if TCom.__instance == None:
            TCom()
        return TCom.__instance


    def __init__(self):
        """ Virtually private constructor. """
        if TCom.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            TCom.__instance = self
            print("Tcom is started")
            # commented while debuging
            self.send("New session is started at " + f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}")


    import telebot
    from telebot import types

    _token = "861287963:AAHCWrZGVUTdb-tqZaaLfzG03BXyXS0L63w"
    _bot = telebot.TeleBot(_token)
    # _bot.polling(none_stop=True, interval=0)

    def send(self, msg = "empty msg", id = 221397150):  # 221397150 - my id
        try:
            self._bot.send_message(chat_id=id, text=str(msg))
        except Exception as e: 
            print("Error:", e)
            return False
        else:
            return True


if __name__ == '__main__':

    # bot.polling(none_stop=True, interval=0)

    TCom1 = Tcom.getInstance()
    TCom1.send("Hi1")
    TCom1.send("Hi2")
    TCom1.send("Hi3")

    # TCom2 = Tcom.getInstance()

