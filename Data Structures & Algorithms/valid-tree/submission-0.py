class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbor_map = {i: [] for i in range(n)}
        for first, sec in edges:
            neighbor_map[first].append(sec)
            neighbor_map[sec].append(first)
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for nbr in neighbor_map[node]:
                if nbr == prev:
                    continue
                if not dfs(nbr, node): return False
            return True
        return dfs(0,-1) and len(visited) == n


