# Compressing a string into its letter, joined by the number of adjacent counts of that letter. Both upper and lower cases are considered. If the compressed string
# is the same length as the original, return the original.
# Time complexity: O(n), space complexity: O(n)

def should_use_original(input_string):
    """Checks if the compression will lead to same length regardless."""
    original_length = len(input_string)
    compressed_length = 2
    letter = input_string[0]

    for i in range(1, len(input_string)):
        if letter != input_string[i]:
            compressed_length += 2
            letter = input_string[i]

    if original_length <= compressed_length:
        return True
    else:
        return False
        

def compress_string(input_string):
    """Compresses string into single letters and its respective counts.
    
    Input: string, to compress
    Output: string, compressed string
    """

    if should_use_original(input_string):
        return input_string

    compressed_string = []
    letter_count = 1
    letter = input_string[0]
    for i in range(1, len(input_string)):
        if letter != input_string[i]:
            # Add to ArrayList
            compressed_string.append(letter)
            compressed_string.append(str(letter_count))

            # Update to new letter
            letter = input_string[i]
            letter_count = 1
        else:
            letter_count += 1
    
    # Append last group of characters
    compressed_string.append(letter)
    compressed_string.append(str(letter_count))

    # Join the ArrayList
    compressed_string = "".join(compressed_string)

    return compressed_string
        

if __name__ == "__main__":
    assert compress_string("aaaabbcc") == "a4b2c2"
    assert compress_string("abc") == "abc"
    assert compress_string("aabbcc") == "aabbcc"
    assert compress_string("aaabbcc") == "a3b2c2"
    assert compress_string("aaaaaaaaaa") == "a10"
    assert compress_string("c") == "c"
    assert compress_string("cc") == "cc"
    assert compress_string("ccc") == "c3"
        
