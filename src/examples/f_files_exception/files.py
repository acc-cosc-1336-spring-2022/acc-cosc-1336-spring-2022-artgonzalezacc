#
def open_file(file_name):
    file_handle = 0
    try:
        file_handle = open(file_name, 'r')
        #work with the file
        print('file opened')
        
        total = 0

        for line in file_handle:
            amount = float(line)
            total += amount

        print("Total: ", total)
        
    except FileNotFoundError:
        print('File ', file_name ,' does not exist...')

    except ValueError as err:
        print(err)

    else: 
        print('No errors occurred')

    finally:
        print('Finally...')
        if(file_handle != 0):
            print('close file')
            file_handle.close()
            