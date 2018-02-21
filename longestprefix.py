# -*- coding: utf-8 -*-
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        i = 1
        prefix = strs[0]
        while i < len(strs):
            j = 0
            while j < len(prefix):
                if prefix[j] != strs[i][j]:
                    prefix = prefix[0:j]
                    break
                j += 1
            i += 1
        return prefix


s = Solution()
d1 = ["hey","heyhey","heyllo","heyba","heyll"]
print s.longestCommonPrefix(d1)
