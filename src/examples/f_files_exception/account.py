
import pickle
from src.examples.j_classes.bank_account import BankAccount

def output_class_w_out_pickle():
    file_name = "accounts.dat"
    account = BankAccount(100)
    file_handle = open(file_name, 'w')

    file_handle.write(str(account.get_balance()))

    file_handle.close()

    file_handle = open(file_name, 'r')

    account1 = 0
    for line in file_handle:
        balance = int(line)
        account1 = BankAccount(balance)

    print(account1)#display 100

    file_handle.close()

def output_class_w_pickle():
    file_name = "accounts1.dat"
    account = BankAccount(100)
    file_handle = open(file_name, 'wb')

    #pickle
    pickle.dump(account, file_handle)

    file_handle.close()

    file_handle = open(file_name, 'rb')
    account1 = pickle.load(file_handle)

    print(account1)
    file_handle.close()


def main():
    output_class_w_pickle()

main()

