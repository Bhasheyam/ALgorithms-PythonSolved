# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        if A.next == None or B == 0:
            return A
        i = self.lenth(A)
        B = B % i
        if B == 0:
            return A
        j = 1
        temp = A
        while j < i - B:
            temp = temp.next
            j += 1
        newhead = temp.next
        temp.next = None
        temp2 = newhead
        while temp2.next != None:
            temp2 =temp2.next
        temp2.next = A
        return newhead
    
    
    def lenth(self, A):
        temp = A
        i = 0 
        while temp:
            i += 1
            temp = temp.next
        return i