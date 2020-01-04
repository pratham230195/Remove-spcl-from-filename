def remove_spl_char(filename):
    for char in filename:
        if char in list_of_spclchar:
            filename = filename.replace(char,"")
    return(filename)


filename = input('Enter the name of the file: ')

list_of_spclchar = ['\\', '/', '. ', '?' ,'*', '|']

file_name = remove_spl_char(filename)
print(file_name)