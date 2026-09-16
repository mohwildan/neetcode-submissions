# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:

        def dfs(root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
            if not root1:
                return root2
            if not root2:
                return root1

            combine_value = root1.val + root2.val
            combine = root1
            combine.val = combine_value

            combine.left = dfs(root1.left, root2.left)
            combine.right = dfs(root1.right, root2.right)

            return combine
        

        return dfs(root1, root2)
 