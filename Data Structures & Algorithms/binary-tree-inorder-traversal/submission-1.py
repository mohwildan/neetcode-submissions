# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder_traversal(self, root: Optional[TreeNode], result: List[int]) -> List[int]:
        if not root:
            return []
        self.inorder_traversal(root.left, result)
        result.append(root.val)
        self.inorder_traversal(root.right, result)
        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        return self.inorder_traversal(root, result)

 