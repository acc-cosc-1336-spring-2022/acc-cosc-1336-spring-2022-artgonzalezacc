def test_config():
    return True

def display_numbers(num):
    cnt = 0
    while cnt < num:
        print(cnt + 1)
        cnt = cnt + 1 #statement that makes the boolean expression cnt < num false

def sum_of_squares(num): #1*1 + 2*2 + 3*3 = 14
    cnt = 0
    sum = 0
    while cnt <= num:
        sum = sum + cnt**2 
        cnt += 1 #statement to make boolean expression false

    return sum

def prompt_user():
    keep_going = 'y'

    while keep_going == 'y':
        keep_going = input("Loop again, type y?") #statement to make boolean expression false

def for_intro_loop():
    for num in [1,2,3,4,5]:
        print(num)

def for_intro_loop_strings():
    for name in ['Winken', 'Blinken', 'Nod']:
        print(name)

def for_num_range(val):
    for num in range(val):
        print(num, "hello world!")

def for_num_range_w_start_value(num, num1):
    for val in range(num, num1):
        print(val)

def for_num_range_w_step_value(num, num1, num2):
    for val in range(num,num1, num2):
        print(val)

def for_display_sum_of_squares(num, num1):
    for val in range(num, num1):
        square = val ** 2
        print(val, '\t', square)

def get_sum(num): # 1 + 2 + 3 = 6
    sum = 0
    count = 0

    while(count <= num):
        sum += count 
        count += 1

    return sum

def get_sum_for(num):#1 + 2 + 3 =
    sum = 0

    for n in range(num):
        sum += n + 1

    return sum

def demo_sentinel():
    lot_number = -1

    while lot_number != 0:
        lot_number = input('Enter lot number (1-10) or 0 to exit')
        
        if(lot_number.isnumeric()):
            lot_number = int(lot_number)   

            if(lot_number != 0):
                while(lot_number < 1 or lot_number > 10):
                    lot_number = input('number must be from 1 to 10')
                    lot_number = int(lot_number)   

            print(lot_number)
        else:
            print("Must be a number")

def nested_loop(row, col):
    for i in range(row):
        print("outer loop-wait for inner loop ", i)
        for j in range(col):
            print("\t inner loop ", j)
        print("inner loop complete")

def nested_loop_while(row, col):
    i = 0
    while(i < row):
        print("outer loop-wait for inner loop ", i)
        j = 0
        while(j < col):
            print("\t inner loop ", j)
            j += 1
        i += 1
        print("inner loop complete")

def multiplication_table_for(row, col):
    for i in range(1,col):
        for j in range(1,row):
            print(str(i*j).rjust(3, " "), end=" ")
        print(' ')
        
def multiplication_table_while(row, col):
    i = 0
    while i < row:
        j = 0
        while j < col:
            product = (i+1)*(j+1)
            print(str(product).rjust(3, " "), end= " ")
            j += 1
        i += 1
        print(' ')

def display_menu():
    print('1-Option 1')
    print('2-Option 2')
    print('3-Exit')

def run_menu():
    option = -1    

    while option != 3:
        display_menu()
        option = int(input("Select menu option"))
        option = handle_option(option)
       
def handle_option(option):

    if option == 1:
        print('Selected option 1')
        return option
    elif option == 2:
        print('Selected option 2')
        return option
    else:
        choice = input("Are you sure, enter y or n")

        if(choice == 'n'):
            return -1
        else:
            print('Program will exit')
            return option













