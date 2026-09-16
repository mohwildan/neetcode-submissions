# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and q or p and not q:
                return False

            if not p or not q:
                return True

            left = dfs(p.left, q.left)
            righ = dfs(p.right, q.right)

            if p.val != q.val:
                return False

            return  left & righ
        return dfs(p, q)
 