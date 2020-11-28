# Moving negative numbers to one side
def moveNegative(arr, lengthArray):
    j = 0
    for i in range(lengthArray):
        if int(arr[i]) < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j+1
    return arr

# [-1 4 5 6 -7]
# temp = arr[4] = -7
#arr[4] = arr[1] = 4
#arr[1] = -7


# Driver code
inputArr = []
lengthArray = int(input())
for i in range(lengthArray):
    numInput = input()
    inputArr.append(numInput)

print(moveNegative(inputArr, lengthArray))
