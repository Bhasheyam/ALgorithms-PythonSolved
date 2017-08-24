def rotate( nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp=nums[k:]
        print(temp)
        nums[k:]=[]
        print(nums)
        nums=temp+nums
        print(nums)
print(rotate([1],0))
        