def removeDuplicates(nums):
        i = 0
        while True:
            print (i,i+1,len(nums),nums[i])
            print(nums)
            if len(nums)- 1 <= i:
                break
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1
            
        return nums

print(removeDuplicates([1,1,2,2,3,4,5,5,6,7,8,9,10,10]))