def cal_median(numbers):
    # print(numbers)
    n = len(numbers)
    if n%2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2])//2
    return numbers[n//2]

n = int(input())

numbers = list(sorted(map(int, input().rstrip().split())))
# print(numbers)
middle = n//2
if n%2 != 0:    
    print(cal_median(numbers[:middle]))
    print(cal_median(numbers))
    print(cal_median(numbers[middle+1:]))
else:
    print(cal_median(numbers[:middle]))
    print(cal_median(numbers))
    print(cal_median(numbers[middle:]))
