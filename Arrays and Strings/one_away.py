# Given two strings, determine if the strings are one insertion, one deletion, or one replacement away (letterwise) from being identical.
# Time complexity: O(n), space complexity: O(1)

def check_for_replacement(string_one, string_two):
    """Checks if two strings are one replacement away from being identical. Subset of problem."""

    is_there_difference = False
    for i in range(len(string_one)):
        if string_one[i] != string_two[i]:
            if is_there_difference:
                return False
            else:
                is_there_difference = True

    return True


def check_for_insertion(string_one, string_two):
    """Checks if two strings are one insertion away from being the same. Subset of problem."""

    index_one = 0
    index_two = 0

    for i in range(len(string_one)):
        if string_one[index_one] != string_two[index_two]:
            if index_one != index_two:
                return False
            else:
                index_one += 1
        else:
            index_one += 1
            index_two += 1
    
    return True


def determine_if_one_away(string_one, string_two):
    """Checks if two strings are one edit away from being identical.
    
    Inputs: string_one, string_two = strings
    Ouputs: boolean, representing True if they are indeed one edit away from being the same.
    """

    # Handling edge cases
    difference_length = len(string_one) - len(string_two)
    if abs(difference_length) > 1:
        return False
    elif string_one == string_two:
        return True

    if difference_length == 0:
        return check_for_replacement(string_one, string_two)
    elif difference_length == 1:
        return check_for_insertion(string_one, string_two)
    elif difference_length == -1:
        return check_for_insertion(string_two, string_one)


if __name__ == "__main__":
    assert determine_if_one_away("place", "pace")
    assert determine_if_one_away("pace", "bace")
    assert determine_if_one_away("plae", "place")
    assert determine_if_one_away("place", "place")
    assert not determine_if_one_away("somewhere", "asdasdasdasdasd")
    assert not determine_if_one_away("somewhere", "asd")
    assert not determine_if_one_away("somewhere", "someshese")