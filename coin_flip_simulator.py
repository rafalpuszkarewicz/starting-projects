import random

def coin_flip(n):
    heads_count = 0
    tails_count = 0
    
    for _ in range(n):
        side = random.choice(['Heads','Tails'])
        if side == 'Heads':
            print('Heads')
            heads_count += 1
        else:
            print('Tails')
            tails_count += 1

    print("Heads count: {} \nTails count: {}".format(heads_count, tails_count))

coin_flip(20)