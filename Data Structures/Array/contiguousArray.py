# Find the largest size of contiguous sub array
# Kadane's algorithm
# https://www.youtube.com/watch?v=86CQq3pKSUw

def largestSum(arr, lengthArray):
    max_current = arr[0]
    max_global = arr[0]

    for i in range(1, lengthArray):
        max_current = max(arr[i], arr[i] + max_current)

        if max_current > max_global:
            max_global = max_current

    return max_global


# Driver code
lengthArray = int(input())
arr = list(map(int, input().strip().split()))

print(largestSum(arr, lengthArray))
