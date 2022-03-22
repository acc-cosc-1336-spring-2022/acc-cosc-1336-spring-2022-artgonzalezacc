#main program
import strings

#strings.hello_world()
#strings.loop_string("hello")
#strings.loop_string_w_while("hello")

#str = "Four score and seven years ago"
#sub_string = "sevenn"

#if strings.string_sub_string(str, sub_string):
#print(sub_string + " in " + str)
#else:
# print(sub_string + " not in " + str)

str = "Four score and seven years ago"

word_list = str.split()
print(word_list)

for word in word_list:
    print(word)