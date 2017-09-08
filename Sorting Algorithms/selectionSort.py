def selection(inputarray):
    i=0
    while i<len(inputarray)-1:
        j=i+1
        while(j<len(inputarray)):
            if(inputarray[i]>inputarray[j]):
                temp=inputarray[i]
                inputarray[i]=inputarray[j]
                inputarray[j]=temp
            j+=1
        i+=1
    return inputarray

#test
print(selection([3,4,52,52,5,2,-4,-1,-6,5]))
print(selection([3,-1,60,50,4,52,52,5,2,-4,-1,-6,5]))
        
        
            