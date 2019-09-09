import random


class Lotto:
    def __init__(self, drawn_nums, total_nums):
        self.drawn_nums = drawn_nums
        self.total_nums = total_nums

    def draw(self):
        all_nums = list(range(1, self.total_nums + 1))
        chosen = []

        while len(chosen) < self.drawn_nums:
            num = random.choice(all_nums)
            chosen.append(num)
            all_nums.remove(num)

        chosen.sort()

        return chosen


# lotto - 6 z 49
# lotto = Lotto(6, 49)


# mini lotto - 5 z 42
# mini_lotto = Lotto(5, 42)

# esktra pensja - 5 z 35 i 1 z 4
# ekstra_5 = Lotto(5, 35)
# ekstra_1 = Lotto(1, 4)


def lotto_sim(play_num):
    lotto = Lotto(6, 49)
    number_of_0 = 0
    number_of_1 = 0
    number_of_2 = 0
    number_of_3 = 0
    number_of_4 = 0
    number_of_5 = 0
    number_of_6 = 0

    game_num = 0
    game_cost = 0

    while game_num < play_num:
        drawn_nums = lotto.draw()

        # append to the file
        #with open("lotto-draw.txt", "a+") as f:
        #    for nums in drawn_nums:
        #        f.write("{}\n".format(nums))

        game_num += 1
        game_cost += 3

        guessed_nums = 0
        # check drawn numbers with one picked by the user
        for num in picked_nums:
            if num in drawn_nums:
                guessed_nums += 1

        if guessed_nums == 1:
            number_of_1 += 1
        elif guessed_nums == 2:
            number_of_2 += 1
        elif guessed_nums == 3:
            number_of_3 += 1
        elif guessed_nums == 4:
            number_of_4 += 1
        elif guessed_nums == 5:
            number_of_5 += 1
        elif guessed_nums == 6:
            number_of_6 += 1
        else:
            number_of_0 += 1

    print(
        "Number of 0 match: {}\nNumber of 1 match: {}\nNumber of 2 match: {}\nNumber of 3 match: {}\nNumber of 4 match: {}\nNumber of 5 match: {}\nNumber of 6 match: {}".format(
            number_of_0,
            number_of_1,
            number_of_2,
            number_of_3,
            number_of_4,
            number_of_5,
            number_of_6,
        )
    )
    print("Total spendings: {} PLN".format(game_cost))
    print("Total winnings: {} PLN".format(number_of_3 * 24 + number_of_4 * 160 + number_of_5 * 5300 + number_of_6 * 1000000 ))


picked_nums = [3, 10, 15, 25, 35, 46]

lotto_sim(1000)

