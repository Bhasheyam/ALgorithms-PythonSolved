'''Given a binary tree t, determine whether 
it is symmetric around its center, 
i.e. each side mirrors the other.'''

#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):
    return mirro(t,t)

def mirro(t,t1):
    if t ==None and t1 == None:
        return True
    if (t is not None and t1 is not None):
            if  t.value == t1.value:
                return (mirro(t.left, t1.right)and
                mirro(t.right, t1.left))
    return False
 