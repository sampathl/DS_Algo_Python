class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
    
class LinkedList:
    def __init__(self, data=None):
        if data==None:
            self.head= None
        else: 
            self.head= Node(data)
    def add(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            pnt= self.head
            while pnt.next != None:
                pnt=pnt.next
            if pnt.next==None:
                pnt.next=Node(data)
    def delete(self):
        self.head= None
    def peek(self):
        return self.head.data
    def pop(self, data=None):
        pnt= self.head
        if self.head==None:
            return None
        elif data==None:
            if self.head.next==None:
                tem=self.head.data
                self.head=None
                return tem
            else:
                while pnt.next.next==None:
                    pnt=pnt.next
                if pnt.next.next==None:
                    temp= pnt.next.data
                    pnt.next=pnt.next.next
                    return temp
        else:
            if self.head.data==data:
                self.head=self.head.next
                return data
            else:
                while pnt.next.data!=data:
                    pnt= pnt.next
                if pnt.next.data==data:
                    pnt.next=pnt.next.next
                    return data

a=LinkedList()
print(a.pop())
a.add(5)
print(a.pop())
a.add(10)
print(a.peek())
b=LinkedList(5)
b.add(10)
print(b.pop(5))
print(b.peek())


