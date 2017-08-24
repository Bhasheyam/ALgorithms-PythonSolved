def maxRotateFunction(A):
        print(len(A))
        ans=0
        for n in A:
            sum=0
            count=0
            a=A.index(n)
            a1=len(A)-a
            if(A.index(n)==0):
                for n1 in A:
                   
                    sum=sum+(n1*count)
                    count=count+1
            else:
                for n1 in A[-a:]:
                   
                    sum=sum+(n1*count)
                    count=count+1
                for n2 in A[:a1]:
                   
                   sum=sum+(n2*count)
                   count=count+1
            print(sum)
            if(A.index(n)==0):
              ans=sum
            if(sum>ans):
                ans=sum
            
               
        return ans
                
            
            
print(maxRotateFunction([4,15,14,3,14,-8,12,-9,17,-1,15,1,10,19,-7,15,8,7,-8,11]))