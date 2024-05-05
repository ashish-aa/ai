graph_edges = [
    (1, 'A', 'B'),
    (3, 'A', 'C'),
    (1, 'B', 'C'),
    (6, 'B', 'D'),
    (5, 'C', 'D'),
    (4, 'C', 'E'),
    (2, 'D', 'E'),
]

vertices = {'A', 'B', 'C', 'D', 'E'}

class DissJointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def makeSet(self,vertice):
        self.parent[vertice] = vertice
        self.rank[vertice] = 0
    
    def find(self,vertice):
        if self.parent[vertice]!= vertice:
            self.parent[vertice] = self.find(self.parent[vertice])
        return self.parent[vertice]
    
    def uninon(self,v1,v2):
        r1 = self.find(v1)
        r2 = self.find(v2)

        if r1!= r2:
            if self.rank[r1]>self.rank[r2]:
                self.parent[r2] = r1
            elif self.rank[r2]>self.rank[r1]:
                self.parent[r1] = r2
            else:
                self.parent[r2] = r1
                self.rank[r1] +=1

def kruskal(vs,es):
    d = DissJointSet()
    for v in vs:
        d.makeSet(v)
    es.sort()
    mst = []

    for e in es:
        w,x,y = e
        if d.find(x)!= d.find(y):
            d.uninon(x,y)
            mst.append(e)

    return mst

mst = kruskal(vertices, graph_edges)

# Display the MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(f"{edge[1]} - {edge[2]} : {edge[0]}")

