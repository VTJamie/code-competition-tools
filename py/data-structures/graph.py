class Graph:
    def __init__(self):
        self.adjacencies = {}

    def connect(self, a, b):
        if a not in self.adjacencies:
            self.adjacencies[a] = []
        self.adjacencies[a].append(b)
        if b not in self.adjacencies:
            self.adjacencies[b] = []
        self.adjacencies[b].append(a)

    def disconnect(self, a, b):
        if a in self.adjacencies:
            self.adjacencies[a].remove(b)

        if b in self.adjacencies:
            self.adjacencies[b].remove(a)


    def getDepthsFrom(self, a, totalnodes):
        depths = [None]*totalnodes
        depths[a] = 0
        curnodes = [a]        
        curdepth = 0
        while len(curnodes) > 0:
            curdepth += 1
            nextnodes = []
            for n in curnodes:
                if n in self.adjacencies:
                    for an in self.adjacencies[n]:
                        if depths[an] == None:                                        
                            depths[an] = curdepth
                            nextnodes.append(an)

            curnodes = nextnodes

        return depths

    def getLeaves(self):
        leaves = []
        for k in self.adjacencies:
            if len(self.adjacencies[k]) == 1:
                leaves.append(k)

        return leaves


if __name__ == '__main__':
    import sys
    import StringIO

    oldstdin = sys.stdin
    data = None
    with open ("data.txt", "r") as myfile:
        data=myfile.readlines()
    sys.stdin = StringIO.StringIO(''.join(data))

    t = int(raw_input())
    print(t)
    for i in range(t):
        n,m = [int(value) for value in raw_input().split()]
        graph = Graph()
        for i in range(m):
            x,y = [int(x) for x in raw_input().split()]
            graph.connect(x-1,y-1) 
        s = int(raw_input())
        depths = graph.getDepthsFrom(s-1, n)
        sarr = []
        for i in range(len(depths)):
            if i != s-1:
                if depths[i] != None:
                    sarr.append(str(depths[i]*6))
                else:
                    sarr.append(str(-1))
        print(' '.join(sarr))   
    
