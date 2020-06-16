n = int(input())

numbers = list(map(int, input().rstrip().split()))
weights = list(map(int, input().rstrip().split()))

total_sum = 0
for i, j in zip(numbers, weights):
    total_sum += i*j
print(round(total_sum/sum(weights), 1))
