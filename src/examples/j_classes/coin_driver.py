
from src.examples.j_classes.coin import Coin
class CoinDriver:

    def __init__(self):#constructor-initialize class attributes/variables
        self.__my__coin = Coin() #instance of coin under __my_coin

    def inspect_result(self):
        return self.__my__coin.get_result() #get result is accessible from another class