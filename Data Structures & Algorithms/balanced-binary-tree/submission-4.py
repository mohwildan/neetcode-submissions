# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        def dfs(root: Optional[TreeNode], i: int):
            if not root:
                return 0,True

            left_i, left_valid = dfs(root.left, i)
            right_i, right_valid = dfs(root.right, i)

            diff = abs(left_i - right_i)
            balance = right_valid and left_valid and diff <= 1

            return 1 + max(left_i, right_i), balance

        _, valid = dfs(root, 0)

        return valid
