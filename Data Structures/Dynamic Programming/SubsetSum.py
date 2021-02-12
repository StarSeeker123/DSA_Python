#Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
#Example:

#Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
#Output:  True // There is a subset(4, 5) with sum 9.

#PROBLEM STATEMENT LINK: https: // www.geeksforgeeks.org/subset-...​

#Playlist Link: https: // www.youtube.com/watch?v = nqowU...​''

def subsetExists(val,W,n):
    sum = 0
    if(n==0):
        return 0
    
    sum = subsetExists(val[n-1]+subsetExists(val,W,n-1))
    
    



#Driver code

val = [3,34,4,12,5,2]
W = 9
n = len(val)
print(subsetExists)


