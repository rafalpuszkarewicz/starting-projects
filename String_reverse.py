def string_reverse():
    '''Enter a string and the program will reverse it and print it out'''
    get_string = input("Enter a string to reverse: ")
    string_reversed = get_string[::-1]
    print(string_reversed)

string_reverse()