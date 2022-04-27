class BankAccount:
    __balance = 0

    def __init__(self,balance): #constructor
        self.__balance = balance

    def deposit(self, amount):
        if(amount > 0):
            self.__balance += amount

    def withdraw(self, amount):
        if(amount > 0 and amount <= self.__balance):
            self.__balance-= amount

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')