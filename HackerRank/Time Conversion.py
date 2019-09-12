def timeConversion(s):
    #
    # Write your code here.

    time_of_day = s[-2:]
    hour = s[:2]
    min_sec = s[2:-2]

    # being provided with time in AM or PM, check for the last two symbols
    if time_of_day.lower() == "pm":
        if int(hour) != 12:
            hour = str(int(hour) + 12)

    else:
        if int(hour) == 12:
            hour = "00"

    return "{}{}".format(hour, min_sec)


s = "07:05:45PM"

