import random

def test_config():
    return True

def local_variable(val0):
    val = val0
    val0 = 100
    val2 = 10
    return val

def main(val0):
    val = 0
    local_variable(val0)

VAL3 = 10 
def use_global():
    VAL3 = 5
    #print(VAL3)
    
#print("global call ", VAL3)
def get_random_number(min, max):#user defined function
    return random.randint(min, max)#python library function

#random.seed(10)
def display_random_numbers(min, max, cnt):#void function

    for i in range(cnt):
        print(random.randint(min,max))

def return_first_last_name():
    return "john", "doe"


