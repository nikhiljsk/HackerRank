def cal_median(numbers):
    # print(numbers)
    n = len(numbers)
    if n%2 == 0:
        return round((numbers[n//2 - 1] + numbers[n//2])/2, 1)
    return round(float(numbers[n//2]), 1)

n = int(input())

numbers = list(map(int, input().rstrip().split()))
frequencies = list(map(int, input().rstrip().split()))

arr = list()
for i, j in zip(numbers, frequencies):
    arr.append([i]*j)

from itertools import chain
arr = sorted(list(chain(*arr)))

# print(arr)
n = len(arr)
middle = n//2
if n%2 != 0:    
    print(cal_median(arr[middle+1:]) - cal_median(arr[:middle]))
else:
    print(cal_median(arr[middle:]) - cal_median(arr[:middle]))
