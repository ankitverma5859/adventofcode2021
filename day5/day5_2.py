import numpy as np

filename = "data.txt"
dataPoints = []
rows = 1000
cols = 1000
overlap_matrix = np.zeros(shape=(rows, cols), dtype=int)


def load_data():
    global filename
    file = open(filename, "r")
    lines = file.read().split('\n')
    for line in lines:
        point, point1, point2 = [], [], []
        p1, p2 = line.replace(" ", "").split('->')
        x1, y1 = p1.split(',')
        point1.append(x1)
        point1.append(y1)
        x2, y2 = p2.split(',')
        point2.append(x2)
        point2.append(y2)
        point.append(point1)
        point.append(point2)
        dataPoints.append(point)


def valid_points(point1, point2):
    if point1[0] == point2[0] or point1[1] == point2[1]:
        return True
    else:
        return False


def get_point(x, y):
    line_point = []
    line_point.append(x)
    line_point.append(y)
    return  line_point


def find_line_points(point1, point2):
    line_points, line_point = [], []
    x1 = int(point1[0])
    y1 = int(point1[1])
    x2 = int(point2[0])
    y2 = int(point2[1])

    if x1 == x2:   #(0,3)-> (0,7) or (0,7)->(0,3)
        if y1 < y2:
            for point in range(y1, y2+1):
                line_points.append(get_point(x1, point))
        else:
            for point in range(y2, y1+1):
                line_points.append(get_point(x1, point))
    elif y1 == y2:  #(2,4,)->(5,4)    (5,4)->(2,4)
        if x1 < x2:
            for point in range(x1, x2+1):
                line_points.append(get_point(point, y1))
        else:
            for point in range(x2, x1+1):
                line_points.append(get_point(point, y1))
    else: #diagonal case
        a = x1
        b = y1
        c = x2
        d = y2
        line_points.append(get_point(a, b))
        while a != c or b != d:
            if a < c and b < d:
                a = a + 1
                b = b + 1
                line_points.append(get_point(a, b))
            elif a > c and b > d:
                a = a - 1
                b = b - 1
                line_points.append(get_point(a, b))
            elif a < c and b > d:
                a = a + 1
                b = b - 1
                line_points.append(get_point(a, b))
            elif a > c and b < d:
                a = a - 1
                b = b + 1
                line_points.append(get_point(a, b))

    return line_points


def create_overlap_matrix():
    global dataPoints
    for dataPoint in dataPoints:
        line_points = find_line_points(dataPoint[0], dataPoint[1])
        print(f'{dataPoint[0]}->{dataPoint[1]}:{line_points}')
        for itr, point in enumerate(line_points):
            x = int(point[0])
            y = int(point[1])
            overlap_matrix[x][y] = overlap_matrix[x][y] + 1


def count_overlapping_points():
    global rows, cols, overlap_matrix
    overlapping_points = 0
    for x in range(0, rows):
        for y in range(0, cols):
            if overlap_matrix[x][y] > 1:
                overlapping_points = overlapping_points + 1
    print(f'Number of Overlapping Points: {overlapping_points}')


load_data()
create_overlap_matrix()
count_overlapping_points()
