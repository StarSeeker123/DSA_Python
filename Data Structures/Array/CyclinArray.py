# cyclic rotation by
def cylicArray(arr, num_rotations):
    new_array = arr
    for _ in range(num_rotations):

        temp = new_array[0]
        new_array = new_array[1:]
        new_array.append(temp)

    return new_array


# Code Array
num_rotations = int(input())
arr = list(map(int, input().strip().split()))

print("The original array is: ", arr)
print("The cyclic array is: ", cylicArray(arr, num_rotations))
