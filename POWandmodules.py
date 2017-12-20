###
#Implement pow(x, n) % d.

#In other words, given x, n and d,

#find (xn % d)
###



def poewfind(x, n, d):
    oddcount = 1
    loopcount = 0
    mul = 0
    i = n
    if i == 0:
        return 1%d
    elif i == 1:
        return x % n
    while i != 2 or i != 3:
        if i % 2 != 0:
            oddcount = oddcount * x
        loopcount += 1
        i = i //2
        
        
    mul = x*x
    if i == 3:
        oddcount = oddcount * x
    
    
    
    k = 0
    while k < loopcount:
        mul = mul *mul
        k +=1
    mul = oddcount * mul
    
    start = 1
    end = x  
    ans = 0 
    while (start <= end) :
        mid = (start + end) // 2
         
        if (mid*d == x) :
            return 0
             
        
        if (mid * d < x) :
            start = mid + 1
            ans = mid
             
        else :
             
            # If mid*mid is greater than x
            end = mid - 1
    return x - ans * d
            
            
            
            
    
    
        
    