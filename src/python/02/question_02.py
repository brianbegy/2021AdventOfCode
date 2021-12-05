import os
import functools


def answer(input_path, use_aim=False):
    commands = read_commands_from_file(input_path)
    position = __get_position(commands, use_aim)
    return position['x'] * abs(position['y'])


def read_commands_from_file(path):
    my_file = open(path, "r")
    result = list(my_file.readlines())
    my_file.close()
    return result


def __get_position(commands, use_aim=False):
    x = 0
    y = 0
    aim = 0
    for command in commands:
        split_command = command.split(' ')
        if(split_command[0] == 'forward'):
            x = x + int(split_command[1])
            if(use_aim):
                y -= int(split_command[1]) * aim
        if(split_command[0] == 'up'):
            if(use_aim):
                aim += int(split_command[1])
            else:
                y += int(split_command[1])
        if(split_command[0] == 'down'):
            if(use_aim):
                aim -= int(split_command[1])
            else:
                y -= int(split_command[1])
    return {"x": x, "y": y}
