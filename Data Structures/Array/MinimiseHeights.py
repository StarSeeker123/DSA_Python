# Minimize the maximum height between

def minimizeHeight(arr, l, k):
    arr.sort()
    max_height = arr[l-1] - arr[0]
    small = arr[0] + k
    big = arr[0] - k

    for i in range(1, n-1):

        subtract = arr[i] - k
        add = arr[i] + k

        if (subtract >= small or add <= big):
            continue

        if (big - subtract <= add - small):
            small = subtract
        else:
            big = add

    return min(ans, big - small)


# Driver code
arr = [4, 6]
n = len(arr)
k = 10

print("Maximum difference is", getMinDiff(arr, n, k))
