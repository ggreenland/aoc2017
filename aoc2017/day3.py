

def spiral_position_generator():
    pos = [0, 0]
    dx = 1
    dy = 0
    while True:
        yield pos
        pos[0] += dx
        pos[1] += dy
        if dx == 1 and pos[0] + pos[1] == 1:
            dx = 0
            dy = 1
        elif dx == -1 and pos[0] == -pos[1]:
            dx = 0
            dy = -1
        elif dy == 1 and pos[0] == pos[1]:
            dx = -1
            dy = 0
        elif dy == -1 and pos[0] == pos[1]:
            dx = 1
            dy = 0


def calc_spiral_distance(val):
    '''
    Find the position (x,y) of a value in the spiral pattern
    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

    :param val:
    :return:
    '''
    cur = 0
    for pos in spiral_position_generator():
        cur += 1
        if cur == val:
            return abs(pos[0]) + abs(pos[1])


def neighbours(pos):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                yield [pos[0] + dx, pos[1] + dy]


def pos_str(pos):
    return str(pos[0]) + str(pos[1])


def find_closest_spiral_sum(val):
    '''

    Find the first value that is larger than the provided value in the spiral pattern
    where each value is the sum of the surrounding values that have already been traversed
    147  142  133  122   59
    304    5    4    2   57
    330   10    1    1   54
    351   11   23   25   26
    362  747  806--->   ...


    :param val:
    :return:
    '''
    values = {}
    for pos in spiral_position_generator():
        if pos == [0,0]:
            values[pos_str(pos)] = 1
        else:
            values[pos_str(pos)] = sum([values[pos_str(p)] for p in neighbours(pos) if pos_str(p) in values])
        if values[pos_str(pos)] > val:
            return values[pos_str(pos)]


if __name__ == "__main__":

    assert calc_spiral_distance(1) == 0
    assert calc_spiral_distance(12) == 3
    assert calc_spiral_distance(23) == 2
    assert calc_spiral_distance(1024) == 31


    value = 368078
    print('Spiral distance for value {} = {}'.format(value, calc_spiral_distance(value)))

    assert find_closest_spiral_sum(0) == 1
    assert find_closest_spiral_sum(748) == 806

    print('First spiral sum value larger than {} = {}'.format(value, find_closest_spiral_sum(value)))
