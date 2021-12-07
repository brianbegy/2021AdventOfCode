import re
import enum


class Rules(enum.Enum):
    NO_DIAGONALS = 0
    DIAGONALS = 1


def get_adjustment(n, n1):
    if(n < n1):
        return n+1
    if(n > n1):
        return n-1
    return n


def get_points(x, y, x2, y2, points):
    key = f'x{x}y{y}'
    points[key] = 1
    if(x == x2 and y == y2):
        return points
    return get_points(get_adjustment(x, x2), get_adjustment(y, y2), x2, y2, points)


def answer_a(path):
    return count_intersections(read_entries_from_file(path), Rules.NO_DIAGONALS)


def answer_b(path):
    return count_intersections(read_entries_from_file(path), Rules.DIAGONALS)


def count_intersections(vectors, rules):
    points = {}
    for vector in vectors:
        if(rules == Rules.DIAGONALS or
                (vector['x1'] == vector['x2'] or vector['y1'] == vector['y2'])):
            xs = [vector['x1'], vector['x2']]
            ys = [vector['y1'], vector['y2']]
            vector_points = get_points(xs[0], ys[0], xs[1], ys[1], {})
            for key in vector_points:
                if key in points:
                    points[key] += 1
                else:
                    points[key] = 1
    count = 0
    for entry in points:
        if(points[entry] > 1):
            count += 1
    return count


def read_entries_from_file(path):
    my_file = open(path, "r")
    content = list(my_file.read().splitlines())
    my_file.close()
    p = re.compile("(\d+),(\d+)\s->\s(\d+),(\d+)")
    vectors = []
    for line in content:
        m = p.match(line)
        vectors.append({"x1": int(m.group(1)), "y1": int(m.group(2)),
                        "x2": int(m.group(3)), "y2": int(m.group(4))})
    return vectors
