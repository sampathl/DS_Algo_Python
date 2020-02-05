"""Implements the pre order transversal(root,left,right) for a tree """

class Pre_order_transversal():
    def __init__(self):
        self.root=None

    def pre_order_transversal(self, pnt):
        """ implements the pre order transversal for a tree, pnt is the reference to root of the tree """
        if pnt.data:
            print(pnt.data, end="\t")
        if pnt.left:
            self.pre_order_transversal(pnt.left)
        if pnt.right:
            self.pre_order_transversal(pnt.right)
        return