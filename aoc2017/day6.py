import copy


def distribution_cycle(banks):
    '''
    Perform a memory distribution by selecting the bank with the most blocks
    and distributing them across all the blocks starting from the bank larger
    than the current

    :param banks:
    :return:
    '''
    cur = banks.index(max(banks))
    blocks = banks[cur]
    banks[cur] = 0
    while blocks > 0:
        cur = (cur + 1) % len(banks)
        banks[cur] += 1
        blocks -= 1


encode_banks = lambda x: ','.join([str(i) for i in x])


def distribute(banks):
    '''
    Distribute the blocks within the banks until a infinite loop is detected.  A loop
    occurs when the bank configuration occurs which has already occurred

    :param banks: list of number of blocks per bank
    :return: number of cycle until infinite loop
    '''
    cycles = 0
    banks = copy.copy(banks)
    config = encode_banks(banks)
    configs = {}
    while not config in configs:
        configs[config] = cycles
        distribution_cycle(banks)
        cycles += 1
        config = encode_banks(banks)
    return (cycles, cycles - configs[config])


if __name__ == "__main__":
    assert distribute([0, 2, 7, 0])[0] == 5

    with open('data/day6_input.txt', 'r') as inputfile:
        banks = [int(i) for i in inputfile.readline().split()]

    num, size = distribute(banks)
    print ('Number of cycles = {}, Loop size = {}'.format(num, size))
