#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    i=2
    key=arr[-1]
    while i <= n and arr[n-i] > key:
        arr[n-i+1]=arr[n-i]
        i+=1
        printArr(arr, n)
    arr[n-i+1]=key
    printArr(arr, n)

def printArr(arr, n):
    for i, e in enumerate(arr):
        print(e, "", end="")
        if i!=0 and (i+1) % n == 0:
            print()

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
