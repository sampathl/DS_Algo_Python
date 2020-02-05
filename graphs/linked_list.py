""" implements a linked list for ajacency list """

class Node():
    
    def __init__(self,node):
        """impements a node for graph in adjacency list repesentations"""
        self.node=node
        self.next=None
    

class linked_list():
    def __init__(self,node_name):
        self.root=Node(node_name)

    def _add_edge_node(self,noden):
        node_name=noden.node
        pnt=self.root
        while pnt:
            if pnt.node==node_name:
                print("this edge already existis")
                return
            pnt=pnt.next
        pnt.next=noden

