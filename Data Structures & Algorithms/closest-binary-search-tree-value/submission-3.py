# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val if root else 0
        def dfs(root: Optional[TreeNode]):
            nonlocal closest

            if not root:
                return

            if abs(target - root.val) < abs(target - closest):
                closest = root.val

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return closest
