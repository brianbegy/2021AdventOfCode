
def answer_a(path):
    return get_fish(read_entries_from_file(path), 80)


def answer_b(path):
    return get_fish(read_entries_from_file(path), 256)


def get_fish(initial_state, iterations):
    ages = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, }
    for i in range(0, len(initial_state)):
        if ages[initial_state[i]] in ages:
            ages[initial_state[i]] = ages[initial_state[i]]+1
        else:
            ages[initial_state[i]] = 0

    for day in range(0, iterations):
        new_fish_count = ages[0]
        ages[0] = ages[1]
        ages[1] = ages[2]
        ages[2] = ages[3]
        ages[3] = ages[4]
        ages[4] = ages[5]
        ages[5] = ages[6]
        ages[6] = ages[7] + new_fish_count
        ages[7] = ages[8]
        ages[8] = new_fish_count

    fish_count = 0
    for age in ages:
        fish_count = fish_count + ages[age]
    return fish_count


def read_entries_from_file(path):
    my_file = open(path, "r")
    content = my_file.read()
    my_file.close()
    return list(map(int, content.split(',')))
