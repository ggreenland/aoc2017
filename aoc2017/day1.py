def calc_consecutive_sum(seq):
    '''
    Calculate the sum of all integers when the previous integer matches the current

    :param seq:
    :return:
    '''
    seq = seq[-1] + seq
    chars = [int(i) for i in seq]
    f = lambda x, y: x + y[0] if y[0] == y[1] else x + 0
    return reduce(f, zip(chars, chars[1:]), 0)


def calc_sum_half_match(seq):
    '''
    Calculate the sum of all digits where the digit at position i matches the digit at position
    (i + N/2) % N where N is the length of the list

    :param seq:
    :return:
    '''
    return reduce(lambda x,y: int(x) + int(y), [seq[i] for i in range(len(seq)) if seq[i] == seq[(i + len(seq) / 2) % len(seq)]], 0)


if __name__ == "__main__":
    # Consecutive sum assert (calc_consecutive_sum('1122') == 3)
    assert (calc_consecutive_sum('1111') == 4)
    assert (calc_consecutive_sum('91212129') == 9)

    with open('data/day1_input.txt', 'r') as file:
        data = file.read().strip()
    print('Sum (consecutive match) = {}'.format(calc_consecutive_sum(data)))

    # half match sum
    assert (calc_sum_half_match('1212') == 6)
    assert (calc_sum_half_match('1221') == 0)
    assert (calc_sum_half_match('123425') == 4)
    assert (calc_sum_half_match('123123') == 12)

    print('Sum (half match) = {}'.format(calc_sum_half_match(data)))
