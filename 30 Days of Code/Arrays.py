#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    # for i in reversed(arr):
    #     print(i, end=' ')
    
    # for i in range(len(arr)):
    #     print(arr[len(arr)-1-i], end=' ')

    for i in range(len(arr)):
        print(arr[-1*(i+1)], end=' ')
