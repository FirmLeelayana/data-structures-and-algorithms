# Given a string and the number of characters, return an edited string that replaces all whitespace with %20.
# Time complexity is O(n), space complexity is O(n).

def convert_whitespace_to_sequence(sequence, length):
    """Converts whitespace to %20 sequence. Returns this new sequence.
    
    Input: Sequence, string of characters to be changed
           Length, integer length of sequence
    Output: Modified string sequence
    """

    series = "%20"
    new_sequence = sequence.split(" ")
    new_sequence = series.join(new_sequence)

    return new_sequence

if __name__ == "__main__":
    print(convert_whitespace_to_sequence("Mr John Doe", 3)) == "Mr%20John%20Doe"
    