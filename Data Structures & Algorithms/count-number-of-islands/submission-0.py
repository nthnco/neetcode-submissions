class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        ans = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    q.append([r,c])
                    while q:
                        y,x = q.popleft()
                        for dy,dx in directions:
                            ny = y + dy
                            nx = x + dx
                            if 0 <= ny < ROWS and 0 <= nx < COLS:
                                if grid[ny][nx] == "1":
                                    grid[ny][nx] = "0"
                                    q.append([ny,nx])
                    ans += 1
        return ans
                        


        

        