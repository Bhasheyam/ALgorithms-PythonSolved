def additionWithoutCarrying(param1, param2):
    i=0
    k=max(len(str(param1)),len(str(param2)))
    t1=str(param1)[::-1]
    t2=str(param2)[::-1]
    ans=" "
    while i < k:
        if( i >= len(str( param1 ) ) ):
            ans = ans + t2[i]
        elif( i >= len(str( param2 ) ) ):
            ans = ans + t1[i]
        else:
           t=int ( t2[i] ) + int( t1[i] )
           ans= ans + str(t%10)
        i += 1
    return int(ans[::-1])



print(additionWithoutCarrying(1234, 898989))

#A little boy is studying arithmetics. He has just learned how to add two integers, written one below another, column by column. But he always forgets about the important part - carrying.

#Given two integers, find the result which the little boy will get.

#Note: the boy used this site as the source of knowledge, feel free to check it out too if you are not familiar with column addition.