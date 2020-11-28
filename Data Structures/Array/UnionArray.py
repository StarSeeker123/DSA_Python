# Union of two arrays


def unionArray(arr1, arr2):
    unionArray = []
    for i in arr1:
        for j in arr2:
            if(i == j):
                unionArray.append(i)
    return set(unionArray)


# Driver code
length_arr1 = int(input())
length_arr2 = int(input())
arr1 = []
arr2 = []

for i in range(length_arr1):
    element_1 = int(input())
    arr1.append(element_1)

for j in range(length_arr2):
    element_2 = int(input())
    arr2.append(element_2)

set_1 = unionArray(arr1, arr2)
for i in set_1:
    print(i)
