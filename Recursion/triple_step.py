# Implement a method to count the number of possible ways a person can run up n steps of stairs if they can hop either 1, 2, or 3 steps.
# O(3^n) time complexity for recursive_hop, O(n) time complexity with memoization, however now takes O(n) space.

import time

def recursive_hop(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return recursive_hop(n-1) + recursive_hop(n-2) + recursive_hop(n-3)


def recursive_memo(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    
    if memo[n] == 0:
        memo[n] = recursive_memo(n-1, memo) + recursive_memo(n-2, memo) + recursive_memo(n-3, memo)
        return memo[n]
    else:
        return memo[n]


def recursive_wrapper(n):
    memo = [0] * (n+1)
    return recursive_memo(n, memo)


if __name__ == "__main__":
    hops = 27

    start = time.time()
    print(recursive_hop(hops))
    end = time.time()
    print(end - start)

    start = time.time()
    print(recursive_wrapper(hops))
    end = time.time()
    print(end - start)