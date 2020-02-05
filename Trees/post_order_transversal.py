"""Implements the post_order_transversal for binary trees"""

class Post_order_transversal():
    def __init__(self):
        self.root=None
    
    def post_order_transversal(self, pnt):

        if pnt.left:
            self.post_order_transversal(pnt.left)
        if pnt.right:
            self.post_order_transversal(pnt.right)
        if pnt.data:
            print(pnt.data, end="\t")
        return
