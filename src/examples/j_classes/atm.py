class ATM:

    def __init__(self, account):
        self.__account = account

    def display_balance(self):
        print(self.__account)

    def deposit(self):
        amount = input("Enter amount to deposit")
        self.__account.deposit(int(amount))

    def withdraw(self):
        amount = input("Enter amount to withdraw")
        self.__account.withdraw(int(amount))