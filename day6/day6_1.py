filename = "data.txt"
init_fish = []


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
    for day in range(0, num_of_days):
        num_of_zeros = count_zeros()
        for itr, fish in enumerate(init_fish):
            if fish > 0:
                init_fish[itr] = init_fish[itr] - 1
            elif fish == 0:
                init_fish[itr] = 6
        for num in range(0, num_of_zeros):
            init_fish.append(8)
    print(init_fish)
    print(f'Number of fishes = {len(init_fish)}')



load_data()
convert_to_int()
calculate_number_of_fishes(80)
