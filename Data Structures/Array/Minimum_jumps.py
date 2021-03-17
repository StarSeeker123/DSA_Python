#Minimum Jumps required for the array
def minimum_jumps(num,n):
    minJumps = [n]*n
    minJumps[0]=0
    for i in range(n):
        for j in range(i+1,min(i+1+num[i],n)):
            minJumps[j] = min(minJumps[j], 1 + minJumps[i])

    return minJumps

    


#Driver code

num = [2,3,1,1,4]
n = len(num)
print(minimum_jumps(num,n))
