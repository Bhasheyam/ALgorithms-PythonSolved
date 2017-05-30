#Given "abcabcbb", the answer is "abc", which the length is 3.

#Given "bbbbb", the answer is "b", with the length of 1.

#Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
def lengthOfLongestSubstring(s):
    def repeatit(ss,great):
        s2=[]
        update=great
        for char in list(ss):
            if(char not in s2):
                s2.append(char)
            elif(len(s2)>update):
                return repeatit(ss[ss.index(char)+1:],len(s2))
            else:
                return repeatit(ss[ss.index(char)+1:],update)
        return s2,update
    su=filter(str.isalpha, s)
    se,great=repeatit(su,0)
    if len(se)>great:
        return len(se)
    else:
        return great       
 
print(lengthOfLongestSubstring("dfdsgsdbsdfesfasvsdfsfasv"))