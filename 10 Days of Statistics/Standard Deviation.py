def cal_mean(numbers):
    return sum(numbers)/len(numbers)

n = int(input())
numbers = list(map(int, input().split()))

mean = cal_mean(numbers)

std = 0
for i in numbers:
    std += ((mean - i)**2)

std /= len(numbers)
print(round(std**(1/2), 1))
