class linkedsingly:
    def __init__(self):
        self.head = None
        
   
    # add element in the last
    def append(self,datas):
       
        if  self.head == None:
            self.head = Node(datas);
        else:
            temp=self.head
            while temp.getnext() != None:
                temp = temp.getnext()
            temp.setNext(Node(datas))

    
    
    # add element first
    
    def insert(self, datas):
        temp = Node(datas)
        temp.setNext( self.head )
        self.head =  temp
    
    def deleteDuplicates(self, A):
        seen = []
        temp = A
        prev = None
        while temp:
            if temp.data in seen:
                    prev.next = temp.next
            else:
                seen.append(temp.data)
                prev = temp

            temp = temp.next
        return A
    
    # remove element from first
    def removefirst(self):
        if self.head == None:
            print("List is Empty")
            return 0
        else:
            self.head = self.head.getnext()
    
    
   
    #Remove elementfrom Last
    
    def pop(self):
        if self.head == None:
            print("List is Empty")
            return 0
        if self.head.getnext() == None:
            self.head = None
        else:
            temp = self.head
            while True:
                if temp.getnext().getnext() == None:
                    temp.setNext(None)
                    break
                temp = temp.getnext()
    
    # add element after k
    def addk(self,k,data1):
        
        temp = self.head
        while temp:
            if temp.getdata() == k:
                new = Node(data1)
                new.setNext(temp.getnext())
                temp.setNext(new)
            temp = temp.getnext()
        
    # remove k element in the List
    def removek(self,k):
        if self.head.getdata() == k:
            self.head= self.head.getnext()
        else:
            temp=self.head
            while temp:
                if temp.getnext() == k:
                    temp.setNext( temp.getnext().getnext())
                temp = temp.getnext()           
    # print the list.
    def printlist(self):
        loop =self.head
        while loop:
            print(loop.getdata())
            loop =  loop.getnext()
           
    def mergeTwoLists(self, A, B):
        ans = Node(0)
        temp = ans
        while A or B:
            if B == None:
                temp.next = A
                break
            elif A == None:
                temp.next = B
                break
            else:
                if A.data <= B.data:
                    temp.next = Node(A.data)
                    A = A.next
                    temp = temp.next
                else:
                    temp.next = Node(B.data)
                    B = B.next
                    temp = temp.next
        return ans.next
      
        
            
        
        
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    # accessing the node    
    def getdata( self ):
        return self.data
        
    def getnext( self ):
        return self.next
        
    def setdata( self, data1 ):
        self.data = data1
        
    def setNext( self, next1 ):
        self.next = next1

listfirst = linkedsingly()
listfirst.append(10)
listfirst.append(20)
listfirst.append(30)
listfirst.append(30)
listfirst.append(30)

Aa=listfirst.deleteDuplicates(listfirst.head)
listfirst1 = linkedsingly()
listfirst1.append(15)
listfirst1.append(25)
listfirst1.append(35)
dd = listfirst1.mergeTwoLists(Aa ,listfirst1.head)

while dd:
    print dd.data
    dd = dd.next
    