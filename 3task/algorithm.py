import random
import time
from collections import Counter

size = 1000000
seq = []
count = 0
for x in range(size):
    seq.append(random.randint(1, 1000))
    count += 1    

def secondMoment(seq):
    c = Counter(seq)
    return sum(v ** 2 for v in c.values())


def AMSestimate(seq, num_samples):
    inds = list(range(len(seq)))
    random.shuffle(inds)
    inds = sorted(inds[: num_samples])

    d = {}
    for i, c in enumerate(seq):
        if i in inds and c not in d:
            d[c] = 0
        if c in d:
            d[c] += 1
    print("0 moment: ", len(d))
    print("1st moment", size)
    return int(len(seq) / float(len(d)) * sum((2 * v - 1) for v in d.values()))


b = secondMoment(seq)
a = AMSestimate(seq, 100)
print("2nd moment: ", b)
print("2nd moment by ams from 100: ", a)
print(abs(b - a))
c = AMSestimate(seq, 500)
print("2nd moment: ", b)
print("2nd moment by ams from 500: ", c)
print(abs(c - a))
