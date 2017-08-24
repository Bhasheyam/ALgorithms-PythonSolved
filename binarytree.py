class tnew():
    def __init__(self,rootid):
        self.left=None
        self.right=None
        self.rootid=rootid;
    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid
    def insertRight(self,newNode):
        if self.right == None:
            self.right = tnew(newNode)
        else:
            tree = tnew(newNode)
            tree.right = self.right
            self.right = tree
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = tnew(newNode)
        else:
            tree = tnew(newNode)
            self.left = tree
            tree.left = self.left


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print("w1")
            print(tree.getNodeValue())
            print("w2")
            printTree(tree.getRightChild())
            


# test tree

def testTree():
    myTree = tnew("Maud")
    myTree.insertLeft("Bob")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    printTree(myTree)
print(testTree())
        