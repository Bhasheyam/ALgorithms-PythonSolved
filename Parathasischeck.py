def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        collection1 = {"[" : "[", "(" : "(", "{" :"{" }
        collection2 = {"]" :"[" , ")" : "(", "}" :"{" }
        i = 0 
        ans1 = []
        while i < len(s):
            
            if s[ i ] in collection1.keys():
                ans1.insert(0, s[ i ])
                
            if s[ i ] in collection2.keys():
                if len(ans1) != 0 and collection2[ s[ i ] ] == ans1[0]:
                    del ans1[0]
                else:
                    return False
            i += 1
        return len(ans1) == 0