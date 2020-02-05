""" Implements a grap using adjacency list without vertices names(sequtial naming)"""

class Node():
    def __init__(self,node):
        """impements a node for graph in adjacency list repesentations"""
        self.node=node
        self.next=None

class Linked_list():
    def __init__(self):
        self.root=None

    def _add_edge_list(self,node_num):
        new_node=Node(node_num)
        ref=self.root
        if ref:
            while ref.next:
                if ref.node==node_num:
                    print("this edge has already been implemented")
                    return
                ref=ref.next
            if ref.node==node_num:
                print("this edge has already been implemented")
                return
            else:
                ref.next=new_node
        else:
            self.root=new_node
   
    def print_list(self):
        ref=self.root        
        while ref:
            print("-->",ref.node,end='\t')
            ref=ref.next
        print('\n')
            

class Graph_adj_list():
    def __init__(self):
        self.alist=[]
    
    def add_node(self):
        """ adds a node to the list """
        llist=Linked_list()
        self.alist.append(llist)
      

    def add_edge(self,v1,v2):
        """ adds an edge between the nodes v1 and v2"""
        v1=int(v1)
        v2=int(v2)
        for i in range(len(self.alist)):
            if v1 == i:
                self.alist[i]._add_edge_list(v2)
            if v2 == i:
                self.alist[i]._add_edge_list(v1)

    def print_graph(self):
        for i in range(len(self.alist)):
            print(i, end="\t")
            self.alist[i].print_list()
            
if __name__== '__main__':
    x=Graph_adj_list()
    x.add_node()
    x.add_node()
    x.add_node()
    x.add_edge(0,2)
    x.add_edge(0,1)
    x.add_edge(0,1)
    x.print_graph()