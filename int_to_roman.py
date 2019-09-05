class Roman_Numerals:
    def int_to_Roman(self, num):
        # list of unique values and roman symbols
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman = ""
        # index
        i = 0

        while num > 0:
            # for every number of whole values in num, add symbol to roman and substract that value from num
            for _ in range(num // value[i]):
                roman += symbol[i]
                num -= value[i]

            # change index
            i += 1

        return roman

print(Roman_Numerals().int_to_Roman(3671))