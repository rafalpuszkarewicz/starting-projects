def prime(n):

    if n < 2:
        return 0

    primes = [2]

    # current number to be checked
    x = 3

    while x <= n:
        # iterate through every second number between 3 and current number to check if it's divisible by that number

        for num in range(3, x, 2):
            # if so break the loop, and check next number
            if x % num == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    return primes


print(prime(31))

