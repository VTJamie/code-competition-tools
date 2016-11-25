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
                        #curpath["camefrom"][k] = curnode
                        visited.add(k)
                        q.appendleft(k)
                    if k not in visited:
                        visited.add(k)
                        q.appendleft(k)

        distance = -1 if b not in self.paths[a]["shortestweight"] else self.paths[a]["shortestweight"][b]
        return distance#, self.traceBack(self.paths[a]["camefrom"], a, b)


if __name__ == '__main__':
    wg = WeightedGraph()
    wg.addEdge(1, 2, 1)
    wg.addEdge(1, 3, 2)
    wg.addEdge(2, 4, 1)
    wg.addEdge(3, 4, 1)
    print(wg.shortestPath(1, 4))
