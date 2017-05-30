#Reverse of the Integer
def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        print(x)
        sign=x>0
        print(sign)
        temp=abs(x)
        x1=[int(d) for d in str(temp)]
        print(x1)
        if(sign):
            print "working"
        return int(''.join(map(str, x1)))
            
print(reverse(-10))