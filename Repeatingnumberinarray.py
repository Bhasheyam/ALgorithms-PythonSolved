'''
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.
'''

def repeatedNumber(A):
        dup = 0
        seen = []
        i = 0
        t = len(A)
        ans = t * (t+1)//2
        while i < len(A):
            if A[i] in seen:
                dup = A[i]
            else:
                seen.append(A[i])
                ans -= A[i]
            i += 1
        return [dup,ans]
