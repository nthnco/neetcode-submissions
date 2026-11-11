class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        visited = set()
        done = set()
        crs_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            crs_map[crs].append(pre)
        def dfs(crs):
            if crs in visited:
                return False
            if crs in done:
                return True
            visited.add(crs)    
            for pre in crs_map[crs]:
                if not dfs(pre): return False
            output.append(crs)
            done.add(crs)
            visited.remove(crs)
            crs_map[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return []
        return output




        