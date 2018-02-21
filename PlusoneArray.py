def plusOne( digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        i = len(digits) - 1
        while i >= 0:

            if digits[i] + 1 >= 10:
                digits[i] = 0
                
            else:
                digits[i] = digits[i] + 1
                return digits
            
            i += 1
        digits.insert(0,carry)
        return digits
    

print plusOne([9])