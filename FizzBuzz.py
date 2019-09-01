def fizzbuzz():
    '''Prints the numbers from 1 to 100. 
    Multiples of three print “Fizz” instead of the number. 
    Multiples of five print “Buzz”. 
    Numbers which are multiples of both three and five print “FizzBuzz”'''
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()
