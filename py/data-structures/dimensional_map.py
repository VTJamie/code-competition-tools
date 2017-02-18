class DimensionMap:
    def __init__(self, g):
        self.g = g

    def surrounding(self, p):
        for i in range(max(p[0]-1, 0), min(p[0]+2, len(self.g))):
            for j in range(max(p[1]-1, 0), min(p[1]+2, len(self.g[i]))):
                if (p[0] != i or p[1] != j):                     
                    yield (self.g[i][j], i, j, p[0] == i or p[1] == j)

    def setPoint(self, p, val):
        self.g[p[0]][p[1]] = val

    def getPoint(self, p):
        return self.g[p[0]][p[1]]

    def perimeter(self):
        for i in range(len(self.g)):                
            yield self.g[i][0], i, 0
            yield self.g[i][-1], i, len(self.g[i])-1        
            if i == 0 or i == len(self.g)-1:
                for j in range(1, len(self.g[i])-1):            
                    yield self.g[i][j], i, j                

    def bfs(self, p, valid):
        curlocs = [p]
        visited = set([p])
        while len(curlocs) > 0:
            nextlocs = []
            for c in curlocs:            
                for val, i, j, hv in self.surrounding(c):                       
                    if (i, j) not in visited and valid(val, i, j, hv):                        
                        visited.add((i, j))
                        nextlocs.append((i, j))                
                yield (self.g[c[0]][c[1]], ) + c                
            curlocs = nextlocs
    
    def allValues(self):
        for i in range(len(self.g)):
            for j in range(len(self.g[i])):
                yield self.g[i][j], i, j
                
    def printGrid(self):
        for row in self.g:
            print(''.join(row))