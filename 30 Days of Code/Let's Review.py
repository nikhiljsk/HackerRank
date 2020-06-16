n = int(input())

strings = list()
for i in range(n):
    strings.append(input())

for i in range(n):
    for j in range(len(strings[i])):
        if j%2==0:
            print(strings[i][j], end='')
    print(' ', end='')
    for j in range(len(strings[i])):
        if j%2!=0:
            print(strings[i][j], end='')
    print()
