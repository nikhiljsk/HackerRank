n = int(input())

unsorted = list()
for _ in range(n):
    unsorted_item = input()
    unsorted.append(unsorted_item)

# int to str or str to int convertion is costly. so, just sort lexicographically and then sort by length.
for i in sorted(sorted(unsorted), key=len):
    print(i)
