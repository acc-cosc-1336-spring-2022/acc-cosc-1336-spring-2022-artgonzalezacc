import pickle

def output_w_out_pickle():
    file_name = "phonebook.txt"
    phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

    file_handle = open(file_name, 'w')

    for key, value in phonebook.items():
        file_handle.write(key + " " + value + '\n')

    file_handle.close()

    file_handle = open(file_name, 'r')

    phonebook2 = {}

    for line in file_handle:
        line = line.rstrip('\n')
        tokens = line.split(' ')
        phonebook2[tokens[0]] = tokens[1]

    print(phonebook2)
    file_handle.close()

def output_w_pickle():
    file_name = "phonebook1.dat"
    phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

    file_handle = open(file_name, 'wb')
    #pickle code here
    pickle.dump(phonebook, file_handle)

    file_handle.close()

    file_handle = open(file_name, 'rb')
    
    phonebook2 = pickle.load(file_handle)

    print(phonebook2)
    
def main():
    output_w_pickle()

main()