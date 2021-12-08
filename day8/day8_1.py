from collections import Counter

filename = "data.txt"
data = []


def load_data():
    global data
    file = open(filename, 'r')
    data = file.read().split('\n')


def find_pattern(pattern):
    digit_dict = [{} for _ in range(10)]

    for element in pattern:
        element_dict = Counter(element)
        distinct_chars = len(element_dict)
        if distinct_chars == 2:
            digit_dict[1] = element_dict
        elif distinct_chars == 4:
            digit_dict[4] = element_dict
        elif distinct_chars == 3:
            digit_dict[8] = element_dict
        elif distinct_chars == 7:
            digit_dict[7] = element_dict

    return digit_dict


def find_digits_appear():
    global data
    times_appear = 0
    for line in data:
        pattern_text, output_text = line.split('|')
        pattern = pattern_text[:-1].split(' ')
        output = output_text[1:].split(' ')
        digit_patterns = find_pattern(pattern)
        for _ in output:
            _dict = Counter(_)
            nums = [1, 4, 7, 8]
            for num in nums:
                if _dict == digit_patterns[num]:
                    times_appear = times_appear + 1
    print(f'Times Appear: {times_appear}')


load_data()
find_digits_appear()
