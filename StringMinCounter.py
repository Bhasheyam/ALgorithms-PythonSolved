# Problem statement 
#Input Array have a groupd of String, we need to find the count of the minium alphabet in everry string 
# for the given input :
# string "aaa" in the array B has count 3 of the min alphabet a. 
# when it is compared with the Elements in the Array A it is greate than all the elements
#EX: string "abcd" has only one a(min aplphabet)
# String "aabc" has only 2
#string "bd" has only one min alphabet b

# for the second element "aa" 
#it is greater tha the string "abcd" and "bd"
# so the expected answer is [3,2]
# supose the input is ['abcd' ,'abc','bd'], ['aaa' ,'aa'] then ans will be[3,3]
#supose the input is ['abcd' ,'aabc','bbd'], ['aaa' ,'aa'] then ans will be[3,1] because the last string has 2 b's(b is the minium alphabet)

def solution(A, B):
    C=[]
    for b in B:
        Counter=0
        for a in A:
            temp1=(a.count(min(a)))
            temp2=(b.count(min(b)))
            if(temp2>temp1):
                Counter +=1
        C.append(Counter)
    return C
    
print(solution(['abcd' ,'aabc','bd'], ['aaa' ,'aa']))
