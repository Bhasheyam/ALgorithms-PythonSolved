def findMedianSortedArrays( A, B):
        i = 0
        j = 0
        k = len(A) + len(B)
        median = k // 2
        ans = []
        
        if len(A) != 0 and len(B) != 0:
            
            while i+j <= median:
                
                if A[i] < B[j]:
                    
                    ans.append(A[i])
                    i += 1
                    
                else:
                    
                    ans.append(B[j])
                    j += 1
                print i,j
        else:
            
            if len(A) ==0:
                
                ans = A
                
            else: 
                
                ans = B
        print ans, median        
        if k % 2 == 0:
            return (ans[median] + ans[median - 1]) /2
        else:
            return ans[median]
print findMedianSortedArrays([ -50, -41, -40, -19, 5, 21, 28 ],[ -50, -21, -10 ])