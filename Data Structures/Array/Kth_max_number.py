# Kth maximum number of an array

def K_max_number(arr, k):
    arr.sort()
    return arr[k-1]


# Driver code
n = int(input())
arr = list(map(int, input().strip().split()))
k = int(input())
print(K_max_number(arr, k))
