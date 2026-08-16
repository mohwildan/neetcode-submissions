# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result: List[int] = []
        result += self.inorder_traversal(root.left)
        result.append(root.val)
        result += self.inorder_traversal(root.right)
        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder_traversal(root)
        
        