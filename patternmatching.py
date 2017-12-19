def patternmatch(element, txt):
    pattern = len(element)
    txtlen = len(txt)
    ans = []
    i =0 
    while i < (txtlen - pattern) -1 :
        j = 0
        while j < pattern:
            if txt[i + j] != element[j]:
                break
            j+= 1
            if pattern - 1 == j:
                ans.append(i)
            
        i += 1
    return ans

txt = "AABAACAADAABAAABAA"
pat = "AABA"
print ( patternmatch(pat, txt))