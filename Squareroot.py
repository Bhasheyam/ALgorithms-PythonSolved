def sqrt( A):
        i = 1
        j = A
        ans = 0
        if A == 0 or A == 1 :
            return A
            
        while i <= j:
            temp = (i + j) // 2
            if temp * temp == A:
                return temp
            if temp * temp < A:
                ans = temp
                i = temp + 1
            else:
                j = temp -1
        return ans