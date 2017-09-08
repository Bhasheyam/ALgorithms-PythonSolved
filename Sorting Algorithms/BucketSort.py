# implementation of bucket sort .

def bucket(inputarray):
    d={}.fromkeys( range( min(inputarray) , max(inputarray)+1 ) , 0 )  # creating a hash to store the values
    ans=[]
     
   # increment the value of the number when you find the number in lopp
    aa=0  
    while aa in range( len(inputarray) ):
        t=inputarray[aa]
        d[t] +=1
        aa +=1
    
    # insert the sorted value in list or array
    for k in sorted( d.iterkeys() ):
        for a1 in range( d[k] ):
            ans.append( k )
    return ans

#test
print(bucket([3,4,52,52,5,2,-4,-1,-6,5]))
print(bucket([3,-1,60,50,4,52,52,5,2,-4,-1,-6,5]))
        
        
       