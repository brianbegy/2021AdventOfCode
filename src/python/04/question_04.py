import re
import enum

board_size = 5


class Playing(enum.Enum):
    TO_WIN = 0
    TO_LOSE = 1

# declare a class to represent the board.  Seems heavy, but encapsulates the logic


class board():
    def __init__(self, board_name, size, raw):
        self.board_name = board_name
        self._size = size
        # I want to abuse dictionaries to make this fast.  Avoid On^2 problems by not looping rows, and then looping columns
        # track the columns and how many matches they have
        self._y_matches = [0] * self._size
        # track the rows and how many matches they have
        self._x_matches = [0] * self._size
        # track the actual matched numbers for fast lookups
        self._matches = {}
        # we can use a dictionary because each number only appears once.
        self._numbers = dict()
        # if the raw input isn't a grid of self._size x self._size, bad things happen.
        for y in range(0, self._size):
            numbers = list(map(int, filter(None, re.split('\s+', raw[y]))))
            for x in range(0, self._size):
                self._numbers[numbers[x]] = {"x": x, "y": y}

    def has_bingo(self, number):
        if(not self._numbers.__contains__(number)):
            return False
        self._matches[number] = 1
        coordinates = self._numbers[int(number)]
        self._y_matches[coordinates["y"]] += 1
        self._x_matches[coordinates["x"]] += 1
        return self._x_matches[coordinates["x"]
                               ] == self._size or self._y_matches[coordinates["y"]] == self._size

    def get_sum_of_not_matches(self):
        sum = 0
        for entry in self._numbers:
            if(not self._matches.__contains__(entry)):
                sum += entry
        return sum


def play(path, mode=Playing.TO_WIN):
    game = read_entries_from_file(path)
    boards_with_bingo = {}
    for number in game['numbers']:
        for board in game['boards']:
            if(not board.board_name in boards_with_bingo):
                if(board.has_bingo(number)):
                    if(mode == Playing.TO_WIN):
                        return board.get_sum_of_not_matches() * number
                    boards_with_bingo[board.board_name] = True
                    if(len(boards_with_bingo) == len(game['boards'])):
                        return board.get_sum_of_not_matches() * number


def answer_a(path):
    return play(path, Playing.TO_WIN)


def answer_b(path):
    return play(path, Playing.TO_LOSE)


def read_entries_from_file(path):
    my_file = open(path, "r")
    result = list(my_file.read().splitlines())
    my_file.close()
    numbers = list(map(int, result[0].split(',')))
    boards = []
    for i in range(2, len(result)-(board_size-1), board_size+1):
        board_name = len(boards) + 1
        boards.append(board(board_name, board_size, result[i:i+board_size]))

    return {'numbers': numbers, 'boards': boards}
