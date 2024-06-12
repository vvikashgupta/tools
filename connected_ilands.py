#!/usr/local/bin/python3
class Solution:
    def numIslands(self, grid):
        from collections import defaultdict, deque
        self.isVisited = defaultdict
        def is_valid(r,c,m,n):
            #print('is_valid')
            return r >= 0 and r < m and c >= 0 and c < n and grid[r][c]
        
        def printgrid():
            for a in grid:
                print(a)

        def bfs(r,c):
            d = deque()
            d.append((r,c))
            while d:
                #print(f'd is {d}')
                row,col = d.popleft()
                if is_valid(row-1,col,len(grid), len(grid[0])):
                    grid[row-1][col] = 0
                    d.append((row-1,col))
                if is_valid(row+1,col,len(grid), len(grid[0])):
                    grid[row+1][col] = 0
                    d.append((row+1,col))
                if is_valid(row,col-1,len(grid), len(grid[0])):
                    grid[row][col-1] = 0
                    d.append((row,col-1))
                if is_valid(row,col+1,len(grid), len(grid[0])):
                    grid[row][col+1] = 0
                    d.append((row,col+1))
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    printgrid()
                    islands += 1
                    print(f'Incrementing islands to {islands} at {i}{j}')
                    grid[i][j] = 0
                    bfs(i,j)
                    printgrid()
                    print(f'Incrementing islands to {islands} at {i}{j}')
        return islands

if __name__ == '__main__':
    c = Solution()
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","1"],
      ["0","0","0","0","0"],
      ["0","0","0","1","1"]
    ]
    #print(grid)
    #printme(grid)
    
    print(c.numIslands(grid))
