class In_order_traversal():
    """ implements in order traversal for a binary tree """
    def __init__(self):
        self.root=None
    
    def in_order_traversal(self,pnt):
        """implemnts in order traversal for binary tree pnt is the reference to root of the tree"""
        if pnt.left:
            self.in_order_traversal(pnt.left)
            print(pnt.data,end='\t')
            if pnt.right:
                self.in_order_traversal(pnt.right)
            return
        else:
            print(pnt.data, end='\t')
            if pnt.right:
                self.in_order_traversal(pnt.right)
            return
        
        print("\n completed printing the tree")


