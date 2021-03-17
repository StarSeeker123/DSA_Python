#DulicateNumber
#Reduced space complexity:Change the index of number to be negative
def duplicateNumber(array,n):
    for i in range(n):
        ele = array[i]

        if array[i]<0:
            return abs(array[i])
        else:  
            array[ele-1]=(0-array[ele-1])
        




#Driver code
array = [1,3,4,4,5]
n = len(array)
print(duplicateNumber(array,n))

