#Minimum jumps
def minimum_jumps(num,n,currentPosition):

    if currentPosition>=n-1:
        return 0
    else:
        minJumps = n
        maxSteps = num[currentPosition]
        while(maxSteps>0):
            minJumps = min(minJumps,1+minimum_jumps(num,n,currentPosition+maxSteps))
            maxSteps = maxSteps-1
        return minJumps



#Driver code
num = [2,3,1,1,4]
n = len(num)

print(minimum_jumps(num,n,0))