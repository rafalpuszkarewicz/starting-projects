def getTotalX(a, b):
    # Write your code here
    result = []

    # append result with number in range between two sets that is divisible by all the numbers in set a
    for num in range(a[-1], b[0] + 1):
        for factor in a:
            divisible = True
            # if number is not divisible by one of the numbers in set a - break the loop
            if num % factor != 0:
                divisible = False
                break
        # if number in range is divisible by all - append to the new list
        if divisible:
            result.append(num)

    total = []

    # check numbers in set b if are divisible by numbers in list from previous check
    for factor in result:
        for num in b:
            divisible = True
            if num % factor != 0:
                divisible = False
                break
        # if yes, append to the total list
        if divisible:
            total.append(factor)

    return len(total)


a = [2, 6]
b = [24, 36]

