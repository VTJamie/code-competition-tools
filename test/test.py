import sys
sys.path.insert(0, '../data-structures')
import dimensional_map


if __name__ == '__main__':    

    def entrypoints(g):
        eps = []
        for val, i, j in g.perimeter():
            if val == '.':                
                eps.append((i, j)) 

        return eps

    def checkforbuildings(c, g):
        for i in range(max(c[0]-1, 0), min(c[0]+2, len(g))):
            for j in range(max(c[1]-1, 0), min(c[1]+2, len(g[i]))):
                if (c[0] != i or c[1] != j) and g[i][j] == 'B':
                    g[c[0]][c[1]] = 'z'
                    return
        
        g[c[0]][c[1]] = 'X'

    def fixup(g):
        for i in range(len(g)):
            for j in range(len(g[i])):
                if g[i][j] == 'X':
                    g[i][j] = '.'
        
    def launchep(ep, g):
        curlocs = [ep]
        while len(curlocs) > 0:
            nextlocs = []
            for c in curlocs:            
                if c[0] > 0 and g[c[0]-1][c[1]] == '.':
                    nextlocs.append((c[0]-1, c[1]))
                if c[1] > 0 and g[c[0]][c[1]-1] == '.':
                    nextlocs.append((c[0], c[1]-1))
                
                if c[0] < len(g)-1 and g[c[0]+1][c[1]] == '.':
                    nextlocs.append((c[0]+1, c[1]))
                if c[1] < len(g[0])-1 and g[c[0]][c[1]+1] == '.':
                    nextlocs.append((c[0], c[1]+1))
                checkforbuildings(c, g) 
            curlocs = nextlocs
            
    print(raw_input())        
    w, h = [int(i) for i in raw_input().split()]
    grid = []
    for i in range(h):
        row = list(raw_input())
        grid.append(row)
    dm = DimensionMap(grid)
    eps = entrypoints(dm)
    for ep in eps: 
        dm.setPoint(ep, 'X')
        #launchep(ep, dm)

    #fixup(grid)

    for row in grid:
        print(''.join(row))