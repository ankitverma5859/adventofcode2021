import numpy as np

filename = "data.txt"
numpy_array = []


def load_data():
    global  numpy_array
    file = open(filename, "+r")
    data = file.read().split('\n')
    digit_array = [[int(num) for num in list(line)] for line in data]
    numpy_array = np.array(digit_array)


def is_low_point(num, r, c, R, C):
    ti, tj = r - 1, c
    di, dj = r + 1, c
    li, lj = r, c - 1
    ri, rj = r, c + 1
    nums = []
    if ti in range(R) and tj in range(C):
        top = numpy_array[ti][tj]
        nums.append(top)
    if di in range(R) and dj in range(C):
        down = numpy_array[di][dj]
        nums.append(down)
    if li in range(R) and lj in range(C):
        left = numpy_array[li][lj]
        nums.append(left)
    if ri in range(R) and rj in range(C):
        right = numpy_array[ri][rj]
        nums.append(right)

    # returns True if all the numbers(x's) in nums are greater than num
    return all(x > num for x in nums)


def heightmap_sum():
    s = numpy_array.shape
    total = 0
    for r in range(s[0]):
        for c in range(s[1]):
            if is_low_point(numpy_array[r][c], r, c, s[0], s[1]):
                print(numpy_array[r][c])
                total = total + (numpy_array[r][c] + 1)
    print(f'Total: {total}')


load_data()
heightmap_sum()
