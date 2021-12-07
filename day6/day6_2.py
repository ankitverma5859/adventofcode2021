import numpy as np
from collections import defaultdict, Counter

filename = "data.txt"
init_fish = np.array(0)


def load_data():
    global init_fish
    file = open(filename, "r")
    data = file.read()
    init_fish = data.split(",")


def convert_to_int():
    global init_fish
    for itr, fish in enumerate(init_fish):
        init_fish[itr] = int(fish)


def count_zeros():
    global init_fish
    count = 0
    for fish in init_fish:
        if fish == 0:
            count = count + 1
    return count


def calculate_number_of_fishes(num_of_days):
    global init_fish
    fish_life_counter = Counter(init_fish)
    for day in range(num_of_days):
        new_fish_life_counter = defaultdict(int)
        for fish_life, count in fish_life_counter.items():
            if fish_life == 0:
                #
                # if the fish_life_time has reached, its life time will be reset to 6
                # and will give birth to a new fish with life time 8
                new_fish_life_counter[6] += count
                new_fish_life_counter[8] += count
            else:
                #
                # if the fish_life_time is not 0 then next day its life time will be
                # reduced by 1
                new_fish_life_counter[fish_life-1] += count
        fish_life_counter = new_fish_life_counter

    print(f'Number of fishes: {sum(new_fish_life_counter.values())}')


load_data()
convert_to_int()
calculate_number_of_fishes(256)
