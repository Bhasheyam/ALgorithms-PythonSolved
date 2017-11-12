'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''
def isPalindrome(A):
        loop = A.strip()
        i = 0 
        ans = ""
        while ( i < len(loop)):
            if loop[i].isalnum():
                ans = ans + loop[i].lower()
            i += 1
        print(ans)
        print(ans[::-1])
        return ans == ans[::-1]
print( isPalindrome("A man, a plan, a canal: Panama"))