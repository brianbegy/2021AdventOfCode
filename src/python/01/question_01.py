import os
import functools


def answer(input_path, step):
    readings = read_list_from_file(input_path)
    return __get_count_of_increased_readings(readings, step)


def read_list_from_file(path):
    my_file = open(path, "r")
    result = list(map(int, my_file.readlines()))
    my_file.close()
    return result


def __sum(a, b):
    """
    is there really no sum function that takes a sequence?
    """
    return a+b


def __get_count_of_increased_readings(readings, step=1):
    count = 0
    max_index = len(readings)-(step-1)
    for i in range(1, max_index, 1):
        old_val = 0
        new_val = functools.reduce(__sum, readings[i:i+step])
        old_val = functools.reduce(__sum, readings[i-1:i+step-1])

        if new_val > old_val:
            count += 1
    return count
