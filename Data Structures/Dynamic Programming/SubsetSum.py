#Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
#Example:

#Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
#Output:  True // There is a subset(4, 5) with sum 9.

#PROBLEM STATEMENT LINK: https: // www.geeksforgeeks.org/subset-...​

#Playlist Link: https: // www.youtube.com/watch?v = nqowU...​''

def isSubetSum(set_1,n,sum):
    subset = ([[False for i in range(sum + 1)] for i in range(n + 1)])
    # If sum is 0, then answer is true
    for i in range(n + 1):
        subset[i][0] = True

    # If sum is not 0 and set is empty,
    # then answer is false

    for i in range(1, sum + 1):
        subset[0][i] = False
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j<set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j>= set[i-1]:
                subset[i][j] = (subset[i-1][j] or
                                subset[i - 1][j-set[i-1]])
    return subset[n][sum]

    
    

#Driver code
set_1 = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set_1)
if (isSubsetSum(set_1, n, sum) == True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")
