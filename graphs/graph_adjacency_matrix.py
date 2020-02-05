""" Implements the ajacency matrix in graphs with out vertices names (squential naming)"""

class Graph_adj_matrix():
    def __init__(self):
        self.matrix=[]

    def add_node(self):
        vertex=[0]
        if self.matrix:
            for i in range(len(self.matrix)):
                self.matrix[i].append(0)
                vertex.append(0)  
            self.matrix.append(vertex)          
        else:
            self.matrix.append(vertex)

    def add_edge(self,v1,v2):
        v1=int(v1)
        v2=int(v2)
        if v1!=v2:
            self.matrix[v1][v2]=1
            self.matrix[v2][v1]=1
        else:
            print("edge to self is not possible")


    def print_graph(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])


if __name__== '__main__':
    x=Graph_adj_matrix()
    x.add_node()
    x.add_node()
    x.add_node()
    x.add_edge(0,2)
    x.add_edge(0,1)
    x.print_graph()