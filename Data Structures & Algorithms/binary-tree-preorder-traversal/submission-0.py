# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        def dfs(root: TreeNode | None, ans: List):
            if root is None:
                return []

            ans.append(root.val)
            dfs(root.left, ans)
            dfs(root.right, ans)
            return ans 
        return dfs(root, ans = [])
 