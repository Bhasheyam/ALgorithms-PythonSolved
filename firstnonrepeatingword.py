def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        i = 0 
        data = {}
        while i < len(s):
            if(s[i] not in data.keys()):
                data[s[i]] = 1
            else:
                data[s[i]] += 1
            i += 1
        j = 0
        while j < len(s):
            if data[s[j]] == 1:
                return j
            j += 1
        return -1
s = "leetcode"
print firstUniqChar(s)