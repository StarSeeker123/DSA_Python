# Steps to follow in a merge sort
# 1 Split the array into two
# 2 Make a recursive call
# 3 Merge the results


# Function to split the array
def mergeSort(arr, l, h):
    if (l < h):
        mid = (l+h)//2
        mergeSort(l, mid)
        mergeSort(mid+1, high)
        merge(l, mid, h)
