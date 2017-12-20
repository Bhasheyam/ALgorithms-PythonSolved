# -*- coding: utf-8 -*-

##Given an array that is sorted and then rotated around an unknown point. Find if array has a pair with given sum ‘x’. It may be assumed that all elements in array are distinct.

#Input: arr[] = {11, 15, 6, 8, 9, 10}, x = 16
#Output: true
#There is a pair (6, 10) with sum 16

def findpair(Array,s):
    i = 0 
    while True:
        if Array[i] > Array[i + 1]:
            break
        i += 1
    start = (i + 1) % (len(Array))
    end  = i
    
    while start != end:
        if Array[start] +Array[end] == s:
            return True
        if Array[start] +Array[end] < s:
            start = (start + 1) % len(Array)
        else:
            end = (len(Array) + end - 1) % len(Array)
    return False

print findpair([11, 15, 6, 8, 9, 10],14)
            