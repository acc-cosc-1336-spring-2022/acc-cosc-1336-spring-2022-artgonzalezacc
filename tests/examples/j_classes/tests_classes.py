import unittest
from src.examples.j_classes.bank_account import BankAccount

from src.examples.j_classes.coin import Coin
from src.examples.j_classes.coin_driver import CoinDriver

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, True)

    def test_coin_sideup_default_value(self):
        coin = Coin()#create a variable or create an instance of the class
        self.assertEqual(coin.get_result(), "Not tossed")#test get default value

    def test_coin_generates_error_accessing_private_attribute(self):
        coin = Coin()
        with self.assertRaises(AttributeError):
            self.assertEqual(coin.__side_up, "Not tossed")#accessing a public variable

    def test_coin_get_result_accessible_from_another_class(self):
        driver = CoinDriver()

        self.assertEqual(driver.inspect_result(), "Not tossed")

    def test_coin_toss_result_either_heads_or_tails(self):
        coin = Coin() #create instance variable
        coin.toss() # simulate a coin toss
        self.assertEquals(True, coin.get_result() == "Heads" or coin.get_result() == "Tails")
        self.assertEquals(True, coin.get_result() == "Heads" or coin.get_result() == "Tails")

    def test_coin_generates_error_accessing_private_method(self):
        coin = Coin()

        with self.assertRaises(AttributeError):
            self.assertEqual("I am private", coin.__get_data())

    def test_coin_private_method_accessible_within_coin_itself(self):
        coin = Coin()
        self.assertEqual("I am private", coin.get_data())

    def test_bank_account_balance_default_value(self):
        account = BankAccount(100) #create an instance/create an object

        self.assertEqual(100, account.get_balance())

    def test_bank_account_deposit(self):
        account = BankAccount(500)
        account.deposit(50)
        account.deposit(-50)

        self.assertEqual(550, account.get_balance())

    def test_bank_account_withdraw(self):
        account = BankAccount(500)
        account.withdraw(50)

        self.assertEqual(450, account.get_balance())

    def test_bank_account_deposit_and_withdraw(self):
        account = BankAccount(500)
        account.deposit(50)
        self.assertEqual(550, account.get_balance())
        account.withdraw(50)

        self.assertEqual(500, account.get_balance())


    
