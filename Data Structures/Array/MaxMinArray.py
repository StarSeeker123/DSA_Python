# Maximum and minimum element in array

def MaximumElement(arr, lengthArray):
    maximum = 0
    for i in range(lengthArray):
        if int(arr[i]) > int(maximum):
            maximum = arr[i]
    return maximum


def MinimumElement(arr, lengthArray):
    minimum = 100
    for i in range(lengthArray):
        if int(arr[i]) < int(minimum):
            minimum = arr[i]
    return minimum


# Driver code
lengthArray = int(input())
arr = []

for i in range(lengthArray):
    arrElement = input()
    arr.append(arrElement)

print("Maxmimum Element is: ")
print(MaximumElement(arr, lengthArray))
print("Minimum Element is: ")
print(MinimumElement(arr, lengthArray))
