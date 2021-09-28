# This file implements the "IsUnique" problem. Given a string, check that the given string has unique characters - different data structures are allowed.
# This solution is O(n) in time complexity, and O(1) in space.

import string

def is_string_unique(input_string):
    """Checks if input string has unique characters, and returns boolean.

    Input: String
    Output: Boolean, represents if string has unique characters or not.
    """

    alphabet = string.ascii_lowercase
    alphabet_hash_table = {}

    for letter in alphabet:
        alphabet_hash_table[letter] = False

    for letter in input_string:
        if alphabet_hash_table[letter]:
            return False   # Has encountered a duplicate letter
        else:
            alphabet_hash_table[letter] = True

    return True   # No duplicates found

if __name__ == "__main__":
    assert is_string_unique('asd')
    assert not is_string_unique('sas')
    assert not is_string_unique('sssssssssssssss')
    assert is_string_unique('qwertyuiopasd')
             