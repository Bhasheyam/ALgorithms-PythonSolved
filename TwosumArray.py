

# To find the pair of two number in the array which can yeild the target sum.


def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        find=lambda x,y: True if x+y==target else False
        result=[]
        temp=nums
        for x1 in nums:
            temp=temp[1:]
            for y1 in temp:
                if(find(x1,y1)):
                    if(x1==y1):
                        result.append(nums.index(x1))
                        result.append(nums.index(y1,nums.index(x1)+1))
                    else:
                        result.append(nums.index(x1))
                        result.append(nums.index(y1))
                    return result
            
           
 
        return []
       

sample=[2,5,5,11]
target=10
print(twoSum(sample,target))