""" implements an interator for in_order_transversal of binary tree """

class In_order_iterator_2():
    def __init__(self,pnt):
        self.stack=[pnt]

    def next(self):
        if self.stack:
            pnt=self.stack.pop()
            while(pnt.left):
                if (pnt.right):
                    self.stack.append(pnt.right)
                self.stack.append(pnt)
                pnt=pnt.left            
            print(pnt.data, end="\t")
            if pnt.right:
                if pnt.right!=self.stack[-1]:
                    self.stack.append(pnt.right)
                    pnt=pnt.right
            return 1
        return None