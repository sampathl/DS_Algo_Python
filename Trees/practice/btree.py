class Node():
    def __init__(self, data):
        self.data=data
        self.right=None 
        self.left=None
    
def height(node):
    if node==None:
        return 0
    else:
        lheight= height(node.left)+1
        rheight=height(node.right)+1
    if lheight > rheight:
        return lheight
    else:
        return rheight

root= Node("root")
root.left=Node("left")
root.left.left=Node("left")
root.right=Node("right")
print(height(root))
