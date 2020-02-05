""" implemnts a binary tree using the node """
from node import Node 
from level_order_transvesal import Level_order_traversal as bsf
from in_order_traversal import In_order_traversal as ist
from pre_order_transversal import Pre_order_transversal as pst
from post_order_transversal import Post_order_transversal as pot
from pre_order_nonrecursive import Pre_order_nonrecursive as pre_non
from in_order_iterative import In_order_iterator as iot_non
from post_order_iterative import Post_order_iterative as poi 
class Binary_tree():
    """ provides the methods for intiatlizing, setting right and left of treee"""

    def __init__(self,data=None):
        self.root=None
        if data:
            new=Node(data)
            self.root=new
        else:
            print("initalized empty tree with no root")

    def _insert_right(self,pnt,new):
        if pnt.right and pnt.left:
            while (pnt.right or pnt.left):
                pnt=pnt.right
        if not pnt.right:
            pnt.right=new
        elif not pnt.left:
            pnt.left=new
        else: 
            print("there is an issue with code")
    
    def _insert_left(self,pnt,new):
        if pnt.right and pnt.left:
            while (pnt.right or pnt.left):
                pnt=pnt.left
        if not pnt.left:
            pnt.left=new
        elif not pnt.right:
            pnt.right=new
        else: 
            print("there is an issue with code")
    

    def add_right(self,data):
        """add the element in root|| right || left"""
        pnt=self.root
        new=Node(data)
        if pnt:
            if pnt.right and pnt.left:
                pnt=pnt.right
                self._insert_right(pnt,new)
            elif not pnt.right:
                pnt.right=new
                return()
            else:
                pnt.left=new
        else:
            new=Node(data)
            self.root=new
            print("added emelment as the root of the tree")
            return

    def add_left(self,data):
        """add the element in root|| left || right"""
        pnt=self.root
        new=Node(data)
        if pnt:
            if pnt.right and pnt.left:
                pnt=pnt.left
                self._insert_left(pnt,new)
            elif not pnt.left:
                pnt.left=new
                return()
            else:
                pnt.right=new
        else:
            new=Node(data)
            self.root=new
            print("added emelment as the root of the tree")
            return

    def _height(self,pnt):
        "pnt is the reference to the root of the tree whose height is required"
        if pnt:
            if pnt.left or pnt.right:
                lheight=(self._height(pnt.left))+1
                rheight=(self._height(pnt.right))+1
                print("d,l,r",pnt.data,lheight,rheight)
                if lheight>rheight:
                    return lheight
                else:
                    return rheight
            else:
                return 1

        else:
            return 0
    def _print_level(self,pnt,level):
        if level==1:
            print(pnt.data, end='\t')
        else:
            level-=1
            if pnt.left:
                self._print_level(pnt.left,level)
            if pnt.right:                
                self._print_level(pnt.right,level)


    def level_order_traversal(self,pnt):
        """prints the elements of a tree using bread search first method"""
        height= self._height(pnt)
        for level in range(1,height+1,1):
            #print("\n at level :", level)
            self._print_level(pnt,level)
        print("\nfinished printing tree")

bt=Binary_tree()
bt.add_right("root")
bt.add_right("right")
bt.add_right("left")
bt.add_right("rright2")
bt.add_right("rleft2")
bt.add_left("lleft2")
bt.add_left("lright2")
bt.add_right("rrright3")
bt.add_left("llleft3")
pnt=bt.root
print("height:",bt._height(pnt))
a=bsf()#check how to implemet the object calling on function
ioo=ist()#check how to implemet the object calling on function
bsf.level_order_traversal(a,pnt)
ist.in_order_traversal(ioo,pnt)

counter=0
iot_non_obj=iot_non(pnt)
while iot_non_obj.next():
    pass

pso=pst()
print("\n pre order transversal:")
pst.pre_order_transversal(pso,pnt)

counter=0
pre_non_obj=pre_non(pnt)

while counter==0:
    counter=pre_non_obj.next()

poto=pot()
print("\n post order transversal:")
pot.post_order_transversal(poto,pnt)

poi_non_obj=poi(pnt)
while poi_non_obj.next():
    pass
