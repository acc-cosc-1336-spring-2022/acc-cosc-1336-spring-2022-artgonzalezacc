import random

class Coin:
    __side_up = "Not tossed" #private

    def __get_data(self):
        return "I am private"

    def get_data(self):#public
        return self.__get_data()

    def get_result(self):#public
        return self.__side_up

    def toss(self):#public
        if random.randint(0, 1) == 0:
            self.__side_up = 'Heads'
        else:
            self.__side_up = 'Tails'