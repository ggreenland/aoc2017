import copy

def simple_update(pos, seq):
    seq[pos] += 1

def complex_update(pos, seq):
    if seq[pos] >= 3:
        seq[pos] -= 1
    else:
        simple_update(pos, seq)

def number_of_jumps(seq, update_fcn):
    '''

    :param seq:
    :return:
    '''
    pos = 0
    jumps = 0
    seq2 = copy.copy(seq)
    while 0 <= pos < len(seq2):
        next_pos = pos + seq2[pos]
        update_fcn(pos, seq2)
        pos = next_pos
        jumps += 1
    return jumps

if __name__ == "__main__":

    with open('data/day5_input.txt', 'r') as inputfile:
        data = [int(line) for line in inputfile]

    print('Number of jumps = {}'.format(number_of_jumps(data, simple_update)))

    assert number_of_jumps([0, 3, 0, 1, -3], complex_update) == 10
    print('Number of jumps (complex)= {}'.format(number_of_jumps(data, complex_update)))