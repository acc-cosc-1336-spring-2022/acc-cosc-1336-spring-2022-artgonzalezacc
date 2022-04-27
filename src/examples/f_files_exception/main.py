#  #main program
import files

def main():
   files.open_file('sales_data.txt')
    # try:
    #     num = float(input('Enter payroll hours'))
    # except ValueError:
    #     print('Invalid number entered...')


main()



# file_name = 'programming.txt'

# #create file
# programming_file = open(file_name, 'w') 

# #use the file
# programming_file.write('C\n')
# programming_file.write('Difficult\n')
# programming_file.write('LISP\n')
# programming_file.write('Medium\n')
# programming_file.write('Ada\n')
# programming_file.write('Easy\n')

# #close the file
# programming_file.close()

# #open file for reading
# programming_file = open(file_name, 'r')

# language = programming_file.readline()
# #use the file
# while language != '':
#     usability = programming_file.readline()

#     print("Language: ", language.rstrip('\n'), end='')
#     print("Usability: ", usability.rstrip('\n'))

#     language = programming_file.readline()

# #close the file
# programming_file.close()

 