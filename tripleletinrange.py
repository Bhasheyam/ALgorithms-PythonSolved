

# there exsist an triplet or not
def solve( A ):
    i = 0
    while i < len(A) -2:
        j = i + 1
        while j < len(A) - 1:
            l = j +1
            while l < len(A):
                t = float(A[i]) + float(A[j]) + float(A[l])
                print(i,j,l,t)
                if t > 1 and t < 2:
                    print("came",i,j,l,t)
                    return True
                l += 1
            j += 1
        i += 1
    
    return False
print solve([ "2.673662", "2.419159", "0.573816", "2.454376", "0.403605", "2.503658", "0.806191" ])