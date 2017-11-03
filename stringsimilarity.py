def findsimilarity(a,b):
    common=[]
    j=0
    i=max(len(a.split(" ")),len(b.split()))
    if(len(a.split(" "))>len(b.split())):
        while(j<i):
            if(a.split(" ")[j] in b.split(" ")):
                common.append(a.split(" ")[j])
            j+=1
    else:
         while(j<i):
             if(b.split(" ")[j] in a.split(" ")):
                 common.append(b.split(" ")[j])
             j+=1  
         k=0
    ref1=0
    ref2=0
    while(k<len(common)):
        
                     
            
            
        
        
    return common

print(findsimilarity("hey good morning", "hey good night"))
