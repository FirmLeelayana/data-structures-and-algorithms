# Given two ASCII strings, check if one string is the permutation of the other. Permutations are case-sensitive.
# Algorithm has time complexity of O(n), and space complexity of O(1) or O(k).

def are_strings_permutations(string_a, string_b):
    """
    Checks if two strings are permutations of one another; returns False if they are not.

    Input: string_a, an ASCII string. 
           string_b, an ASCII string.
    Outputs: boolean.
    """

    # Checking for edge case where lengths are not equal: clearly not permutations
    if len(string_a) != len(string_b):
        return False

    ascii_alphabet_dict = {}
    for i in range(128):
        ascii_alphabet_dict[chr(i)] = 0

    for letter in string_a:
        ascii_alphabet_dict[letter] += 1

    for letter in string_b:
        ascii_alphabet_dict[letter] -= 1
        if ascii_alphabet_dict[letter] < 0:
            return False   # Represents edge case 2: if negative, that means there exists a character in string_b that doesn't in string_a

    for key, value in ascii_alphabet_dict.items():
        if value != 0:
            return False
    
    return True

if __name__ == "__main__":
    assert are_strings_permutations("some", "mose")
    assert not are_strings_permutations("hand", "tase")
    assert not are_strings_permutations("as", "asd")
    assert not are_strings_permutations("asddd", "asdddddd")