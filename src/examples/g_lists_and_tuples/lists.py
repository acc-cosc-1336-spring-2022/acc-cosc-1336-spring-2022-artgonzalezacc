from src.examples.j_classes.bank_account import BankAccount

def test_config():
    return True

def loop_list_w_for(nums):
    for n in nums:
        print(n)

    nums[0] = 10

def loop_list_w_while(nums):
    indx = 0

    while indx < len(nums):
        print(nums[indx])
        indx += 1

    nums[2] = 0

def collect_home_values():
    home_values = [0] * 5
    indx = 0
    while indx < len(home_values):
        home_values[indx] = int(input('Enter home value: '))
        indx += 1

    for v in home_values:
        print(v)

def find_item_in_list(item1, list1):
    if item1 in list1:
        return True
    else:
        return False

def append_item_to_list(item1, list1):
    list1.append(item1)

def get_gross_pay(hours, pay_rate):
    return hours * pay_rate

def sum_list_items(list1):
    sum = 0

    for num in list1:
        sum += num

    return sum

def return_list():
    list1 = [2,4,6,8,10]

    return list1

def get_2d_list_item(indx, list1):
    return list1[indx]

def get_multiplication_table(max_value):
    table = []

    for r in range(1, max_value):
        row = []
        for c in range(1, max_value):
            row.append(r * c)

        table.append(row)

    return table

def list_of_accounts():
    account1 = BankAccount(100)
    account2 = BankAccount(200)

    list1 = []
    list1.append(account1)
    list1.append(account2)

    for account in list1:
        print(account)

    account1a = list1[0]
    account2a = list1[1]
    print(' ')
    print(account1a)
    print(account2a)





