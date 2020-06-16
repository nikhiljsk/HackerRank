from itertools import product

k, m = list(map(int, input().rstrip().split()))

numbers = list()
for i in range(k):
    numbers.append(list(map(int, input().rstrip().split()))[1:])

total_sum = 0
for i in product(*numbers):
    temp = sum([x**2 for x in i])
    if temp % m > total_sum % m:
        total_sum = temp % m

print(total_sum)
