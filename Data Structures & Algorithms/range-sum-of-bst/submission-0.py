# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:

        def dfs(root: TreeNode | None) -> int:
            if not root:
                return 0

            cal = 0
            if root.val >= low and root.val <= high:
                cal = root.val

            left_cal = dfs(root.left)
            right_cal = dfs(root.right)
            return cal + left_cal + right_cal

        return dfs(root)
 