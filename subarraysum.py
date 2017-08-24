def mat(nums):
    ans=0
    for n in range(len(nums)-1):
        a=find(n,nums)
        if(a>ans):
            ans=a
    return ans
def find(nn,nums):
    ans=0
    for n in range((len(nums)-nn)):
        a=sum(nums[n:n+nn+1])
        if(a>ans):
            ans=a
    return ans
print(mat([1,3,4,1,2,5,5,-100,5,5,5,5,5,-30]))