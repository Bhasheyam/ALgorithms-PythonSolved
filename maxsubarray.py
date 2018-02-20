class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        ans=0
        for n in range(len(nums)):
            a=self.find(n,nums)
            if(a > ans):
                ans=a
        return ans
    def find(self,nn,nums):
        tans=0
        print nn
        for n in range((len(nums)-nn)):
            print n
            a1=sum(nums[n:n+nn+1])
            print a1, nums[n:n+nn+1]
            if(a1 > tans):
                tans=a1
        return tans
s = Solution()
print s.maxSubArray([1,2,3,4,5])