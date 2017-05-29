#Find the length of the harmony array. 
def findLHS(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        great=0
        def setgreat(value):
            if value>=great:
                return value
            return great
        group=list(set(nums))
        temp=group
        def calculatelength(arr):
            update=filter(lambda x: x in arr, nums)
            newvalue=len(update)
            great1=setgreat(newvalue)
            return great1
        for x in group:
            temp=temp[1:]
            for y in temp:
                if x-y== 1 or x-y==-1:
                    values=[]
                    values.append(x)
                    values.append(y)
                    great=calculatelength(values)
        return great
                  
print(findLHS([1,2,2,4,4,5,6,7,5,6]))
# here[4,4,5,5] and [5,6,6,5] are the two harmony array and max lenth is 4.