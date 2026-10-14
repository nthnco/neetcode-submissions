# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, greatest):
            if root is None:
                return 0
            if root.val >= greatest:
                greatest = root.val
                return 1 + dfs(root.left, greatest) + dfs(root.right,greatest)
            else:
                return dfs(root.left, greatest) + dfs(root.right,greatest)
        ans = dfs(root, root.val)
        return ans 

            
            
            

