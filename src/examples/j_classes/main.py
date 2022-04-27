# import coin_driver

# driver = coin_driver.CoinDriver()
# print(driver.inspect_result())
import bank_account
import atm

def main():
    account = bank_account.BankAccount(100)
    my_atm = atm.ATM(account)
    
    print("ACC Bank")
    my_atm.display_balance()
    my_atm.deposit()
    my_atm.display_balance()
    my_atm.withdraw()
    my_atm.display_balance()


    # print(account.get_balance())
    # account.deposit(100)
    # print(account.get_balance())

    # print(account)

main()