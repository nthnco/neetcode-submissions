class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]
        rank = [1] * n
        count = n
        def find(n):
            if n != p[n]:
                p[n] = find(p[n])
            return p[n]
            
        def union(n1, n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                p[p2] = p1
                rank[p1] += rank[p2]
            else:
                p[p1] = p2
                rank[p2] += rank[p1]
            return True
        for n1, n2 in edges:
            if union(n1,n2):
                count -= 1
        return count
        

            
            