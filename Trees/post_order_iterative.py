""" this implements an iterator for post order transversal for a binary tree"""

class Post_order_iterative():
    def __init__(self, pnt):
        self.stack=[]
        while pnt:
            if pnt.right:
                self.stack.append(pnt.right)
            self.stack.append(pnt)
            pnt=pnt.left
        print("\nThis is post order iterative:")

    def next(self):
        counter=0
        pnt=None
        while counter==0 and self.stack:
            while pnt:
                if pnt.right:
                    self.stack.append(pnt.right)
                self.stack.append(pnt)
                pnt=pnt.left
            else:
                pnt=self.stack.pop()
                if self.stack and pnt.right==self.stack[-1]:
                    npnt=self.stack.pop()
                    self.stack.append(pnt)
                    pnt=npnt
                    npnt=None
                else:
                    print(pnt.data,end='\t')
                    pnt=None 
                    counter=1
        
        if not self.stack:
            return None
        return 1

            