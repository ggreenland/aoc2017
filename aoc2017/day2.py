def find_divisor(data):
    '''
    Find divisor of the two values in the list which can be divided without a remainder
    :param data:
    :return:
    '''
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and data[i] % data[j] == 0:
                return data[i] / data[j]


def calc_divisor_sum(data):
    '''
    Calculate the sum of the divisors of the values on each row that can be divided without a remainder
    :param data:
    :return:
    '''
    return sum([find_divisor(row) for row in data])


def calc_checksum(data):
    '''
    Calculate the sum of the difference between the largest and smallest number of each row
    :param data:
    :return:
    '''
    return sum([max(row) - min(row) for row in data])


if __name__ == "__main__":
    assert (calc_checksum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]) == 18)

    with open('data/day2_input.txt', 'r') as file:
        data = [map(int, line.split()) for line in file]
    print('Checksum = {}'.format(calc_checksum(data)))

    assert (calc_divisor_sum([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]) == 9)

    print('Checksum (divisor) = {}'.format(calc_divisor_sum(data)))
