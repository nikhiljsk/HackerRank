n = int(input())

numbers = list(map(int, input().rstrip().split()))

# From Scratch
# Mean
print(round(sum(numbers)/len(numbers), 1))

# Median
n = len(numbers)
numbers = sorted(numbers)
if n%2 == 0:
    print(round((numbers[n//2 - 1] + numbers[n//2])/2, 1))
else:
    print(numbers[n//2 - 1])

# Mode
from collections import defaultdict, OrderedDict
freq_numbers = defaultdict(int)
for i in numbers:
    freq_numbers[i] += 1

# Sort according to keys first, so smallest number is in front
freq_numbers = {k:v for k, v in sorted(freq_numbers.items(), key = lambda x: x[0])}

# Sort according to values
freq_numbers = {k:v for k, v in sorted(freq_numbers.items(), key = lambda x: x[1], reverse=True)}
print(list(freq_numbers.keys())[0])

# Using OrderedDict (maybe key positions are changed). Not really nec in this case atleast
# freq_numbers = OrderedDict(sorted(freq_numbers.items(), key = lambda x: x[0]))
# freq_numbers = OrderedDict(sorted(freq_numbers.items(), key = lambda x: x[1]))

"""
# Using inbuilt
import numpy as np
from scipy import stats

print(np.mean(numbers))
print(np.median(numbers))
print(stats.mode(numbers)[0][0])
"""
