def test_config():
    return True

def hello_world():
    hello = "hello world!12" #string
    print(hello[0])
    print(hello)

def loop_string(str):
    for c in str:#hello
        print(c)

def loop_string_w_while(str):
    indx = 0

    while indx < len(str):
        print(str[indx])
        indx = indx + 1

def concat_strings(str1, str2):
    return str1 + str2

def slice_string(str):
    return str[6:10]

def string_sub_string(str, sub_string):
    return sub_string in str


