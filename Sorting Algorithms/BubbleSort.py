def bubble(inputarray):
    i=len(inputarray)
    while(i>0):   #running the loop for input size to perform the sort everytime
        j=1
        while(j<i):
            if(inputarray[j]<inputarray[j-1]):
                
                temp=inputarray[j-1]
                inputarray[j-1]=inputarray[j]  # performing the swap
                inputarray[j]=temp
            j+=1
        i-=1
    return inputarray
print(bubble([3,4,52,52,5,2,-4,-1,-6,5]))
print(bubble([3,-1,60,50,4,52,52,5,2,-4,-1,-6,5]))
            
    