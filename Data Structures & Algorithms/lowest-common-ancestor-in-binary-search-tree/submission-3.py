# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val:
            less, greater = p.val, q.val

        else:
            greater, less = p.val, q.val

        while root:
            if less < root.val < greater:
                return root
            if root.val == less or root.val == greater:
                return root
            if root.val > greater:
                root = root.left
            else:
                root = root.right
         
