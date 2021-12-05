import os
import functools
import enum


class MostOrLeastCommon(enum.Enum):
    MOST = 0
    LEAST = 1


def answer_a(input_path):
    entries = read_entries_from_file(input_path)
    gamma = __get_common_value(entries)
    epsilon = __get_common_value(entries, False)
    return gamma * epsilon


def answer_b(input_path):
    entries = read_entries_from_file(input_path)
    oxygen_generator_rating = get_most_or_least_commmon(entries)
    co2_scrubber_rating = get_most_or_least_commmon(
        entries, MostOrLeastCommon.LEAST)
    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


def get_most_or_least_commmon(entries, least_common=MostOrLeastCommon.MOST):
    remaining_entries = entries
    for i in range(0, len(entries[0])):

        most_common = __get_most_common_for_position(remaining_entries, i)
        matcher = most_common
        if(least_common == MostOrLeastCommon.LEAST):
            matcher = int(most_common == False)
        was = remaining_entries
        remaining_entries = list(filter(
            lambda entry: int(entry[i]) == matcher, remaining_entries))
        if(len(remaining_entries) == 1):
            return remaining_entries[0]


def __get_common_value(entries, most=True):
    value = ''
    for i in range(0, len(entries[0])):
        val = __get_most_common_for_position(entries, i)
        if(most):
            value += str(val)
        else:
            value += str(int(val == 0))
    return int(value, 2)


def read_entries_from_file(path):
    my_file = open(path, "r")
    result = list(my_file.read().splitlines())
    my_file.close()
    return result


def __get_most_common_for_position(entries, position):
    count_zero = 0
    count_one = 0
    for entry in entries:
        if(entry[position] == "1"):
            count_one += 1
        else:
            count_zero += 1

    if(count_one >= count_zero):
        return 1
    return 0
