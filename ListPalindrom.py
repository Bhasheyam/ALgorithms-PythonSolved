
# to check whether a list is palindrom or not

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    ans=[]
    while( l != None ):
        ans.append( l.value )
        l = l.next 
    if len( ans ) == 0:
        return True
    else:
        return  ans == ans[::-1]

