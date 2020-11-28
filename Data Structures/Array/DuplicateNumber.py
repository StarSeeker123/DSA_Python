def duplicateElement(arr):
    arr.sort()
    for i in range(0, len(arr)-1):
        if arr[i] == arr[i+1]:
            return arr[i]

    return -1


# Driver code
arr = list(map(int, input().strip().split()))
print(duplicateElement(arr))
