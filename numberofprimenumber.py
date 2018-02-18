import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 2
        while i <= n-1:
            if self.prime(i):
                count += 1
            i += 1
        return count 
    
    def prime( self, n ):
        i = 2
        n1 = math.floor( math.sqrt( n ))
        while i <= n1:
            if n % i == 0:
                return False
            i += 1
        return True