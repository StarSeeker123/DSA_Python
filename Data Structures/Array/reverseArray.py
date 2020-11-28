# Beginning with the data structures and algorithms
# Reverse array

def reverseArray(arr):
    reverseArray = arr[::-1]
    return reverseArray


inputArr = []
lengthArray = int(input())
for i in range(lengthArray):
    numInput = input()
    inputArr.append(numInput)

print(reverseArray(inputArr))
