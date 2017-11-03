#Two sorted Array find k lements of the array.
def findk(a,b,k):
    i=0
    j=0
    ans=[]
    while(i+j<k):
        if a[i]<b[j]:
            ans.append(a[i])
            i+=1
        else:
            ans.append(b[j])
            j+=1
    return ans
            

print(findk([1,4,6,7,8],[2,3,4,6,7],5))