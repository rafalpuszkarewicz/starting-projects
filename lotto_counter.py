def counter(total_nums):

    with open("ekstra_pensja-draw.txt", "r") as f:
        all_drawn_nums = []
        for item in f:
            all_drawn_nums.append(int(item))

    for num in range(1, total_nums + 1):
        print("Number of {}: {}".format(num, all_drawn_nums.count(num)))


counter(35)
