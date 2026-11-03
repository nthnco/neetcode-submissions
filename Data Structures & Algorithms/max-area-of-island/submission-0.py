class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        ans = 0
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    q.append([r,c])
                    cur_sum = 1
                    while q:
                        y, x = q.pop()
                        for dy, dx in directions:
                            ny, nx = dy + y, dx + x
                            if 0 <= ny < ROWS and 0 <= nx < COLS:
                                if grid[ny][nx] == 1:
                                    grid[ny][nx] = 0
                                    q.append([ny,nx])
                                    cur_sum += 1
                    ans = max(cur_sum, ans)
        return ans
                



        