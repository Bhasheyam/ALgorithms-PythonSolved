def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        d = {key:value for key, value in zip( nums,range(len(nums)))}
        while i < len(nums) - 1:
            temp = target - nums[i]
            if(temp in d.keys() and d[temp] != 1):
                return [i,d[temp]]
            i += 1
                
        return []

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))