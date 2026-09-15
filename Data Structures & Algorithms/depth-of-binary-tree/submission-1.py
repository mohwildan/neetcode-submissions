# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode], count: int) -> int:
            if not root:
                return 0

            left = dfs(root.left, count)
            right = dfs(root.right, count)

            return count + 1 + max(left, right)
        return dfs(root, 0)
