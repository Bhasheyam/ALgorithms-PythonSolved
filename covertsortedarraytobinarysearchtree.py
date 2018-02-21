# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.treegen(0,len(nums),nums)
    
    
    def treegen(self, start,end,nums):
        if start >= end:
            return None
        mid = (start + end ) / 2
        root = TreeNode( nums[ mid ] )
        root.right = self.treegen(mid + 1,end ,nums)
        root.left = self.treegen( start, mid,nums)
        return root
        
    