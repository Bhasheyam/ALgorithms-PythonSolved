'''
Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.
'''
#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    if t == None :
        return s == 0
    values =  [[t,t.value]]
    while( len(values) > 0):
        currentstate = []
        i = 0 
        while( i < len(values)):
            if values[i][0].left:
                temp = values[i][1] + values[i][0].left.value
                currentstate.append([values[i][0].left,temp])
            if values[i][0].right:
                temp = values[i][1] + values[i][0].right.value
                currentstate.append([values[i][0].right,temp])            
            i += 1
        if len(currentstate) == 0:
            i = 0
            while( i < len(values)):
                if( s in values[i]):
                    return True 
                i += 1
            return False
        else:
            values = currentstate
    


