from collections import Counter
import statistics
import sys

filename = "data.txt"
data_list = []
data_dict = {}
summation, avg, median, sd = 0, 0, 0, 0


def load_data():
    global data_list
    with open(filename) as file:
        data_list = [int(x) for x in file.read().split(',')]


def calculate_statistics():
    global summation, avg, sd, median
    summation = sum(data_list)
    avg = int(round(summation/len(data_list)))
    median = int(statistics.median(data_list))
    sd = int(round(statistics.pstdev(data_list), 0))


def sum_of_natural_numbers(num):
    return (num * (num + 1)) / 2


def find_outcome(number):
    outcome_value = 0
    for item in data_dict:
        steps = abs(item - number)
        outcome_value = outcome_value + (int(sum_of_natural_numbers(steps)) * data_dict[item])
    return outcome_value


def find_cheapest_outcome():
    global data_dict,summation, avg, sd
    print(f'Sum: {summation}')
    print(f'Avg: {avg}')
    print(f'Median: {median}')
    print(f'Standard Deviation: {sd}')
    probable_numbers = range(avg - 10, avg + 10, 1)

    data_dict = Counter(data_list)
    print(data_dict)
    least_outcome = sys.maxsize
    for num in probable_numbers:
        outcome = find_outcome(num)
        if outcome < least_outcome:
            least_outcome = outcome
    print(f'LeastOutcome: {least_outcome}')

load_data()
calculate_statistics()
find_cheapest_outcome()
