def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    a, b = ints[0], ints[0]

    for i in ints :
        a = min(a, i)
        b = max(b, i)
    
    return a, b


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 1000)]
random.shuffle(l)
print(get_min_max(l))
# (0, 9)

print(get_min_max(range(1000)))
# (0, 999)

print(get_min_max(range(1000)[::-1]))
# (0, 999)

print(get_min_max([1]))
# (1, 1)

print(get_min_max([1] * 1000))
# (1, 1)

print(get_min_max([1, 2] * 1000))
# (1, 2)

print(get_min_max([2, 1] * 1000))
# (1, 2)