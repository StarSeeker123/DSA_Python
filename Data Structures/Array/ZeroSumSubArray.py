# Sub array with sum zero
# To create a sub-array

def subArrayExists(arr, n):
    n_sum = 0
    s = set()

    for i in range(n):
        n_sum += arr[i]

        if n_sum == 0 or n_sum in s:
            return True

        s.add(n_sum)
        return False


# Driver Code
subArray = list(map(int, input().strip().split()))


print(subArrayExists(subArray))
