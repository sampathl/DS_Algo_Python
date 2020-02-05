""" stack implementaion  using node.py 

    0| data,prev(null)|1| data,pre |2| """

from node import Node

class Stack():
    #init
    def __init__(self):
        self.head=None
        self.len=0
    #print Stack
    def __print_stack(self):
        #check head
        print(self.len)
        if self.head:
            # for len print elements and move 
            pnt=self.head
            for i in range(self.len,-1,-1):
                print(pnt.data, self.len-i , sep=" at pos ")
                if pnt.prev:
                    pnt=pnt.prev
                else:
                    print("finished printing the stack")
                    return
        else:
            print("no elemenets in stack")


    #push
    def push(self,data):
        """ adds an element to the stack starting from 0 position """
        #create node 
        new=Node(data)
        #assign head to new node pre
        new.prev=self.head
        #assign new node to head
        self.head=new
        self.len+=1


    #pop
    def pop (self):
        if self.head:#check head
            pop_=self.head
            self.head=self.head.prev   #move head to head.prev
            self.len-=1
            print(pop_.data)
        else:
            print("no elements in stack")
        #dec len

    #peek
    def peek(self):
        if self.head:
            print(self.head.data)
        else:
            print("stack is empty")


    #search
    def search(self,data):
        if self.head:
            pnt=self.head
            for i in range(self.len,-1,-1):
                if pnt:
                    if pnt.data==data:
                        print("element at pos", self.len-i)
                        return
                    else:
                        pnt=pnt.prev
        else:
            print("value not in this list")

                    


if __name__ =="__main__":
    pass
    s=Stack()
    s.__print_stack()
    s.push(1)
    s.__print_stack()
    s.push("new")
    s.__print_stack()
    s.pop()
    s.__print_stack()
    s.push("new")
    s.push("hi")
    s.push("hi1")
    s.peek()
    s.__print_stack()
    s.search("new")