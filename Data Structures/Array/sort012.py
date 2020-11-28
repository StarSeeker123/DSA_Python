def sort012(arr, n):
    zeroArray = []
    oneArray = []
    twoArray = []
    for i in arr:
        if i == 0:
            zeroArray.append(i)
        elif i == 1:
            oneArray.append(i)
        else:
            twoArray.append(i)
    return zeroArray + oneArray + twoArray


# Driver code
n = int(input())
arr = list(map(int, input().strip().split()))

print(sort012(arr, n))

#DutchNaturalAlgorithm
#https://www.youtube.com/watch?v=ER4ivZosqCg&t=440s&ab_channel=BackToBackSWE https://www.youtube.com/watch?v=oaVa-9wmpns&t=430s&ab_channel=takeUforward
