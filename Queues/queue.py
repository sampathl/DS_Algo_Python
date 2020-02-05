"""implements a basic queue"""
from node import Node

class Queue():
    
    def __init__(self):
        self.front=None
        self.rear=None
        self.len=0

    def enque(self,data):
        # create node 
        new=Node(data)
        if self.rear:    # check rear 
            self.rear.prev= new
            self.rear=new
            self.len+=1
            # add into que 
            #update rear
        elif not self.front:# if first 
            self.front=new
            self.rear=new
            self.len+=1
            # add into que
            #update front and rear
        else:
            print("there is an issue with the que")
            exit()

    def __print_queue(self):
        if self.rear and self.front:
            pnt=self.front
            for i in range (self.len):
                print("{} at {} ".format(pnt.data,i))
                if pnt.prev:
                    pnt=pnt.prev
                else:
                    print("end")
                    return
        else:
            print("no data in the que")

    def deque(self):
        if self.rear and self.front:
            if self.front:
                pnt=self.front
                self.front=self.front.prev
                self.len-=1
                print(pnt.data)
                pnt.prev=None

            else:
                pnt=self.front
                self.front=None
                self.rear=None
                self.len-=1
                print(pnt.data)
                pnt.prev=None
                if self.len!=0:
                    print("there is an issue")
                    exit()
        else:
            print("no elements in the que ")

            #check first ele 
                # if not one then change front to front.prev
            # if last one change rear and front to none


    def first(self):
        if self.front:
            print("front",self.front.data)
        else:
            print("no data in the list ")
    

    def last(self):
        if self.rear:
            print("rear",self.rear.data)
        else:
            print("no data in the list ")

if __name__=="__main__":

    q=Queue()
    q.__print_queue()
    q.enque(5)
    q.enque(6)
    q.first()
    q.last()
    q.enque(9)
    q.enque(12)
    q.__print_queue()
    q.deque()
    q.first()
    q.last()
    q.__print_queue()

