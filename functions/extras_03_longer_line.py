from math import sqrt, floor


def starting_point(magnitude_1, magnitude_2, point_1, point_2):
    if magnitude_1 < magnitude_2:
        return point_1
    elif magnitude_2 < magnitude_1:
        return point_2
    else:
        return point_1


def magnitude_free(start, end):
    magnitude = sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    return magnitude


x_1 = float(input())
y_1 = float(input())
point_one = [floor(x_1), floor(y_1)]

x_2 = float(input())
y_2 = float(input())
point_two = [floor(x_2), floor(y_2)]

x_3 = float(input())
y_3 = float(input())
point_three = [floor(x_3), floor(y_3)]

x_4 = float(input())
y_4 = float(input())
point_four = [floor(x_4), floor(y_4)]

vector_1 = sqrt(x_1**2 + y_1**2)
vector_2 = sqrt(x_2**2 + y_2**2)
vector_3 = sqrt(x_3**2 + y_3**2)
vector_4 = sqrt(x_4**2 + y_4**2)

start_first = starting_point(vector_1, vector_2, point_one, point_two)
start_second = starting_point(vector_3, vector_4, point_three, point_four)

if start_first == point_one:
    end_first = point_two
    vector_first = magnitude_free(point_one, point_two)
else:
    vector_first = magnitude_free(point_two, point_one)
    end_first = point_one

if start_second == point_three:
    end_second = point_four
    vector_second = magnitude_free(point_three, point_four)
else:
    vector_second = magnitude_free(point_four, point_three)
    end_second = point_three


if vector_first > vector_second:
    print(f"({start_first[0]}, {start_first[1]})({end_first[0]}, {end_first[1]})")
elif vector_second > vector_first:
    print(f"({start_second[0]}, {start_second[1]})({end_second[0]}, {end_second[1]})")
else:
    print(f"({start_first[0]}, {start_first[1]})({end_first[0]}, {end_first[1]})")
