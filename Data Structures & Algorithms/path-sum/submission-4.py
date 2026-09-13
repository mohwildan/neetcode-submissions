# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def backtracking(root: Optional[TreeNode], cal: int):
            if not root:
                return False

            cal += root.val

            if not root.left and not root.right:
                return cal == targetSum
            return backtracking(root.left, cal) or backtracking(root.right, cal)

        return backtracking(root, 0)


