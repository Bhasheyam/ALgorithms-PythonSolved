# given two set of array- Array A is greater than Array B if the first non-match element of the array A is greater than the element of the Array B.
# if the length of the substring is given then we need to use a sliding window to find all the possible consecutive sub-set of the given array.
# for the given example it is [1,4,3,2] and [4,3,2,5]
# then according to first point all the sub-set need to be solved and one greatest subset should be returned
def solution(A, K):
    # write your code in Python 2.7
    i=0
    collection=[]
    while(i<len(A)-K+1):
       collection.append(A[i:i+K])
       i+=1
    k=1
    print(collection)   
    greater=collection[0]
    while(k<len(collection)):
        b=0
        while(b<len(collection[k])):
            if(collection[k][b]==greater[b]):
                b+=1
                continue
            elif(collection[k][b]>greater[b]):
                greater=collection[k]
                break
            else:
                break
        k+=1 
    return greater
print(solution([1,4,3,2,5], 4))
