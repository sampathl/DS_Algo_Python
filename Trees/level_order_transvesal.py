class Level_order_traversal():
    def __init__(self):
        self.height=None
    
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



