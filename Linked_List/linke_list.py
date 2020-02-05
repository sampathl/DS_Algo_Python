""" implemnts a single linked list"""

from node import Node

class sllist():
    def __init__(self):
        self.head=None
        self.len=0

    def __print_list(self):
        pnt=self.head
        if self.head:
            print("length: ",self.len)
            for i in range(1,self.len+1):
                print(pnt.data, i, sep=' at ')
                pnt=pnt.next
        else:
            print("list dose not have any elements")
            

    def append(self, data):
        """ adds a node to the linked list with the given data"""
        new=Node(data)
        if self.len==0:
            self.head=new
        else:
            pnt=self.head
            for y in range(1,self.len):
                print(y)
                pnt=pnt.next
            pnt.next=new
            print("appending:",data)
            #print("last",pnt.next.data)
        self.len+=1

    def insert(self,data,pos):
        
        if self.len>=pos:
            new=Node(data)
            pnt=self.head
            for y in range(1,pos-1,1):
                pnt=pnt.next
            new.next=pnt.next
            pnt.next=new
            self.len+=1
        elif self.len<pos:
            print("error linkedlist is not that long")

    def delete(self,pos):
        if self.len>=pos:
            pnt=self.head
            for y in range (1,pos-1):
                pnt=pnt.next
            pnt.next=pnt.next.next
            self.len-=1
        else:
            print("list is not that long")

    def search(self,data):
        counter=0
        if self.len>0:
            for y in range(1,self.len+1):
                if y==1:
                    pnt=self.head
                else:
                    pnt=pnt.next
                if pnt.data==data:
                    print("element exist in the list at",y)
                    counter+=1
                    return
        if counter==0:
            print("data dose not exit")        

if __name__=="__main__":
    lists=sllist()
    #print("list created")
    lists.__print_list()
    lists.append("new")
    lists.__print_list()
    lists.append(5)
    lists.append(8)
    lists.__print_list()
    lists.delete(2)
    lists.__print_list()
    lists.insert(6,2)
    lists.__print_list()
    lists.search(6)
    lists.search(8)
    lists.search(10)
