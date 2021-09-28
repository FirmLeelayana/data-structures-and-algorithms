# Given a string consisting of only lowercase letters and whitespaces, find if it is a permutation of a palindrome.
# Time complexity: O(n), space complexity: O(1) or O(k), where k is the letters in the alphabet.

import string

def string_is_permutation_of_palindrome(input_string):
    """Checks if the input string given has a permutation that is a palindrome: returns a boolean.
    
    Inputs: string, to be investigated
    Outputs: boolean, representing if string has a palindrome permutation
    """
    # Remove whitespaces
    input_string = input_string.split(" ")
    input_string = "".join(input_string)

    # Create hash table of alphabet
    alphabet = {}
    for letter in string.ascii_lowercase:
        alphabet[letter] = 0

    # Count how many times each letter appears
    for letter in input_string:
        alphabet[letter] += 1

    # Count how many letter has odd frequencies
    odd_count = 0
    for key, value in alphabet.items():
        if (value % 2 == 1):
            odd_count += 1

    # Determine if palindrome permutation exists
    is_even_length = (len(input_string) % 2 == 0)
    if odd_count == 0 and is_even_length:
        return True
    elif odd_count == 1 and not is_even_length:
        return True
    else:
        return False

if __name__ == "__main__":
    assert string_is_permutation_of_palindrome("tact coa")
    assert not string_is_permutation_of_palindrome("tact csoa")
    assert string_is_permutation_of_palindrome("a sd as d")
    assert string_is_permutation_of_palindrome("da da")
    assert not string_is_permutation_of_palindrome("da sa")
