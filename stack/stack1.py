class Node():
    def __init__(self, data):
        self.data=data
        self.next=None

class Stack():
    def __init__(self,data=None):
        if data==None:
            self.head = None
        else:
            self.head = Node(data)
    
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            temp=Node(data)
            temp.next=self.head
            self.head=temp
    
    def pop(self):
        if self.head==None:
            return None
        else:
            temp=self.head
            self.head=self.head.next
            return temp.data
    def peek(self):
        if self.head== None:
            return None
        else:
            return self.head.data
    def isEmpty(self):
        return self.head == None

a= Stack()
a.push(10)
a.push(5)
print(a.pop())
print(a.peek())
a.pop()
print(a.isEmpty())
