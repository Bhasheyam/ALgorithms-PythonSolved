def lengthOfLastWord( s ):
        """
        :type s: str
        :rtype: int
        """
        sa = s.split(" ")
        
        
        
        n = len(sa) - 1
        while n >= 0:
            if s[n] != '':
                return s[n]
        return 0
        
    
print lengthOfLastWord( "a " )
    