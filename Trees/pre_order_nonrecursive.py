""" implements pre order transversal using non recusive method"""

class Pre_order_nonrecursive():

    def __init__(self,pnt):
        self.stack=[pnt]
        print("\n this is pre order iterative :")

    def next(self):
        
        if self.stack:
            pnt=self.stack.pop()
            if pnt:
                print(pnt.data, end="\t")
            if pnt.right:
                self.stack.append(pnt.right)
            if pnt.left:
                self.stack.append(pnt.left)
            return 0
            
        else:
            print("the tree has been preinted")
            return 1


