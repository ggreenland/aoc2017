



def valid_passphrase(words):
    '''
    Determine is passphrase is valid.  Validity is true when the input list does not contain
    duplicates

    :param words:
    :return:
    '''
    return len(set(words)) == len(words)

def valid_passphrase_enhanced(words):
    '''
    Determine is passphrase is valid.  Validity is true when the input list does not contain
    duplicates or any anagrams

    :param words:
    :return:
    '''
    return valid_passphrase([''.join(sorted(word)) for word in words])

if __name__ == "__main__":

    with open('data/day4_input.txt', 'r') as inputfile:
        phrases = [line for line in inputfile]

    num_valid_phrases = sum([1 if valid_passphrase(line.split()) else 0 for line in phrases])
    print('Number of Valid = {}'.format(num_valid_phrases))

    num_valid_phrases = sum([1 if valid_passphrase_enhanced(line.split()) else 0 for line in phrases])
    print('Number of Valid and No Anagrams = {}'.format(num_valid_phrases))
