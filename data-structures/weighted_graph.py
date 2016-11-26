from collections import deque

class WeightedGraph:
    def __init__(self):
        self.nodes = {}
        self.paths = {}

    def addEdge(self, a, b, weight):
        if a not in self.nodes:
            self.nodes[a] = {}
        if b not in self.nodes:
            self.nodes[b] = {}
        if b not in self.nodes[a] or self.nodes[a][b] > weight:    
            self.nodes[a][b] = weight
        if a not in self.nodes[b] or self.nodes[b][a] > weight:
            self.nodes[b][a] = weight
    def traceBack(self, camefrom, a, b):
        tracelist = []
        if b in camefrom:
            curnode = b
            tracelist.append(b)
            while curnode != a:
                tracelist.append(camefrom[curnode])
                curnode = camefrom[curnode]
        return tracelist[::-1]

    def findSetContainingEach(self, treelist, a, b):
        aset = None
        bset = None
        for s in treelist:
            if a in s:
                aset = s
            if b in s:
                bset = s
        return aset, bset
    def smallestSpanningTree(self):
        edgelist = []
        finaledges = []
        treecreated = set()
        trees = []
        for k in self.nodes:
            for k2 in self.nodes[k]:
                edgelist.append((self.nodes[k][k2], k, k2))
                if k not in treecreated:                    
                    treecreated.add(k)
                    trees.append(set([k]))
                if k2 not in treecreated:
                    treecreated.add(k2)
                    trees.append(set([k2]))
        edgelist.sort()
        treecreated = None
        for edge in edgelist:
            if len(trees) == 1:
                break
            aset, bset = self.findSetContainingEach(trees, edge[1], edge[2])
            if aset != bset:
                trees.remove(bset)
                aset.update(bset)
                finaledges.append(edge)

        return finaledges if len(trees) == 1 else None


    def shortestPath(self, a, b):
        if a not in self.paths:              
            self.paths[a] = {
                "shortestweight": {},
                "camefrom": {}
            }
            curpath = self.paths[a]
            self.paths[a]["shortestweight"][a] = 0
            visited = set([a])
            q = deque([a])
            while len(q) > 0:
                curnode = q.pop()
                
                for k in self.nodes[curnode]:
                    weighttonode = self.nodes[curnode][k]       
                    curweight = curpath["shortestweight"][curnode]
                    if k not in curpath["shortestweight"] or curpath["shortestweight"][k] > curweight + weighttonode:
                        curpath["shortestweight"][k] = curweight + weighttonode
                        curpath["camefrom"][k] = curnode
                        visited.add(k)
                        q.appendleft(k)
                    if k not in visited:
                        visited.add(k)
                        q.appendleft(k)

        distance = None if b not in self.paths[a]["shortestweight"] else self.paths[a]["shortestweight"][b]
        return distance, self.traceBack(self.paths[a]["camefrom"], a, b)


if __name__ == '__main__':
    wg = WeightedGraph()
    wg.addEdge(1, 2, 1)
    wg.addEdge(1, 3, 2)
    wg.addEdge(2, 4, 1)
    wg.addEdge(3, 4, 1)
    wg.addEdge(5, 6, 1)
    print(wg.shortestPath(1, 4))
    print(wg.shortestPath(1, 5))
    print(wg.smallestSpanningTree())


