class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue():
    def __init__(self,data=None):
        if data==None:
            self.head=None
            self.tail=None
        else:
            self.head=Node(data)
            self.tail= self.head
    def add(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
        else:
            temp=self.head
            self.head=Node(data)
            self.head.next=temp
        
    def pop(self):
        if self.head==None:
            return None
        elif self.head==self.tail:
            temp=self.head
            self.head=None
            self.tail=None 
            return temp.data
        else:
            pnt= self.head
            while pnt.next.next!=None:
                pnt=pnt.next
            if pnt.next==self.tail:
                temp=pnt.next
                self.tail=pnt
                pnt.next=None
                return temp.data
            
    
    def peek(self):
        if self.tail!=None:
            return self.tail.data
        else:
            return None
    
    def isEmpty(self):
         return self.tail==None and self.head==None

a=Queue()
a.add(10)
print(a.peek())
a.add(12)
a.pop()
print(a.pop())

print(a.isEmpty())        