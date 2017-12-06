

def calc_consecutive_sum(sequence):
    '''
    Calculate the sum of all integers when the previous integer matches the current

    :param sequence:
    :return:
    '''
    sequence = sequence[-1] + sequence
    chars = [int(i) for i in sequence]
    f = lambda x, y: x + y[0] if y[0] == y[1] else x + 0
    return reduce(f, zip(chars, chars[1:]), 0)



if __name__ == "__main__":
    print(calc_consecutive_sum('1122'))
    print(calc_consecutive_sum('1111'))
    print(calc_consecutive_sum('91212129'))

    with open('data/day1_input.txt', 'r') as file:
        data = file.read().strip()
    print('Sum = {}'.format(calc_consecutive_sum(data)))