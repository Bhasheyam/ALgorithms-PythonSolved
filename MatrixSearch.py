class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        i = 0
        while i < len( A ):
            
            if B <= A[i][len(A[i]) -1 ]:
                
                return self.check(A[i],B, len(A[i]) )
                
            i += 1
        return False
    def check(self,A1,B1, i):
        while i != 0:
            if i == 1 and A1[0] != B1:
                return False
            else:
                if A1[i//2] == B1:
                    return True
                elif A1[i//2] > B1:
                    A1 = A1[0:(i//2) ]
                    i = len(A1)
                else:
                        A1 = A1[(i//2):]
                        i = len(A1)
c = Solution()
print(c.searchMatrix([
  [2, 3, 4, 6]
  ,[16, 19, 33, 36]
  ,[37, 38, 38, 41]
  ,[47, 47, 50, 51]
  ,[55, 57, 58, 62]
  ,[63, 65, 66, 66]
  ,[68, 70, 75, 77]
  ,[78, 84, 84, 86]
  ,[86, 87, 88, 92]
  ,[94, 95, 96, 97]

],81))
print(c.searchMatrix( [[22, 32, 67]], 93))
print(c.searchMatrix([[3, 3, 11, 12, 14]
  ,[16, 17, 30, 34, 35]
  ,[45, 48, 49, 50, 52]
  ,[56, 59, 63, 63, 65]
  ,[67, 71, 72, 73, 79]
  ,[80, 84, 85, 85, 88]
  ,[88, 91, 92, 93, 94]], 94))