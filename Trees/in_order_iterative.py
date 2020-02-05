""" implements an interator for in_order_transversal of binary tree """

class In_order_iterator():
    def __init__(self,pnt):
        self.stack=[pnt]
        while(pnt.left):
            self.stack.append(pnt.left)
            pnt=pnt.left
        print("\nIn Order Traversal iterative: ")

    def next(self):
        if self.stack:
            pnt=self.stack.pop()
            print(pnt.data, end="\t")
            if(pnt.right):
                self.stack.append(pnt.right)
                pnt=pnt.right
                while(pnt.left):
                    self.stack.append(pnt.left)
                    pnt=pnt.left
            return 1
        return None