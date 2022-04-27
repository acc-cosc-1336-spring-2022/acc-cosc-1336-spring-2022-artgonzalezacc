def main():
    file_name = "languages.dat"
    list1 = ["C++", "C#", "Java"]
    file_handle = open(file_name, 'w')

    for item in list1:
        file_handle.write(item + '\n')

    file_handle.close()

    file_handle = open(file_name, 'r')

    list2 = []

    for line in file_handle:
        list2.append(line.rstrip('\n'))

    print(list2)

main()

