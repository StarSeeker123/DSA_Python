def mergeArray(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    for i in range(n-1, 0):
        last = arr1[m-1]
        j = m-2
        while(arr1[j] > arr[i]):
            arr[j+1] = arr[j]
            j = j-1
        if (last > arr2[i]):
            arr1[j+1] = arr2[i]
            arr2[i] = last
    return (arr1, arr2)


# Driver code
arr1 = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))

print(mergeArray(arr1, arr2))
