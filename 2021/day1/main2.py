# Noval
import itertools
import collections

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

tot = 0
last = None
for number in sliding_window(open("input.txt"), 3):
    number = sum(int(x.strip()) for x in number)
    if not last:
        print(f"{number} (N/A - no previous measurement)")
    elif last < number:
        print(f"{number} (increased)")
        tot += 1
    elif last > number:
        print(f"{number} (decreased)")
    else:
        print(f"{number} (no change)")
    last = number

print(tot)

# Simple
import itertools
import collections

def sliding_window(iterable, n):
    """ Sliding Window

    From Itertools Examples
    """
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

tot = 0
last = None
for number in sliding_window(open("input.txt"), 3):
    number = sum(int(x.strip()) for x in number)
    if last and last < number:
        tot += 1
    last = number

print(tot)

# Golfing
import collections, itertools 

def sliding_window(iterable, n):
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

print(sum( 1 for x in sliding_window(sliding_window(open("input.txt"), 3), 2) if sum(int(y.strip()) for y in x[0]) < sum(int(y.strip()) for y in x[1])))

