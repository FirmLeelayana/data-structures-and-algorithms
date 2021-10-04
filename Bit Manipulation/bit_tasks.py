# Implementation of some common bit manipulation tasks, such as getting a bit.

def get_bit(num, index):
    """Get the bit at a specified index (starting from 0 at the LSB)."""

    return int(((num & (1 << index)) != 0))


def set_bit(num, index):
    """Set a bit at a specified index to one."""

    return (num | (1 << index))


def clear_one_bit(num, index):
    """Clears a single bit."""

    return num & ~(1 << index)


def clear_left_of_bit(num, index):
    """Clears from MSB to specified index inclusive."""

    return num & ~(-1 << index)


def clear_right_of_bit(num, index):
    """Clears from LSB to specified index inclusive."""

    return num & (-1 << index + 1)


def update_bit(num, index, new_bit):
    """Update bit with the specified new bit."""

    return (num & (1 << index)) | (new_bit << index)


if __name__ == "__main__":
    number = 0b0110 #6
    print(get_bit(number, 0))
    print(set_bit(number, 0))
    print(clear_one_bit(number, 2))
    print(clear_left_of_bit(number, 1))
    print(clear_right_of_bit(number, 1))
    print(update_bit(number, 3, 1))