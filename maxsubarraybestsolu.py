class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        maxa = nums[0]
        check = nums[0]
        i = 1
        while i < len(nums):
            check = max(check + nums[i], nums[i])
            maxa = max(maxa, check)
            i += 1
        return maxa