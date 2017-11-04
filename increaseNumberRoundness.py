'''
Define an integer's roundness as the number of trailing zeroes in it.

Given an integer n, check if it's possible to increase n's roundness by swapping some pair of its digits.

Example

For n = 902200100, the output should be
increaseNumberRoundness(n) = true.

One of the possible ways to increase roundness of n is to swap digit 1 with digit 0 preceding it: roundness of 902201000 is 3, and roundness of n is 2.

For instance, one may swap the leftmost 0 with 1.

For n = 11000, the output should be
increaseNumberRoundness(n) = false.

Roundness of n is 3, and there is no way to increase it.
'''
def increaseNumberRoundness(n):
    n1=str(n).count("0")
    i=0
    t1=str(n)[::-1]
    count=0
    while i < len( t1 ):
        if t1[i] == "0" :
            count += 1
            i += 1
        else:
            if(count< n1):
                return True 
            else:
                return False
        
        
    return False
    
    

print(increaseNumberRoundness(12301342000))