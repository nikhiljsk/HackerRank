n = int(input())

phonebook = dict()
for i in range(n):
    name, number = input().split()
    phonebook[name] = number

import sys
read = sys.stdin.read()
queries = read.split('\n')

for query in queries:
    try:
        print("{0}={1}".format(query, phonebook[query]))
    except KeyError:
        print("Not found")
