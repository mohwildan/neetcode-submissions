# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_i = 0
        def dfs(root: Optional[TreeNode], i: int):
            nonlocal max_i
            if not root:
                return 0

            left_h = dfs(root.left, i)
            right_h = dfs(root.right, i)
            max_i = max(max_i, left_h + right_h)
            return i + 1 + max(left_h, right_h)
        dfs(root, 0)
        return max_i
 