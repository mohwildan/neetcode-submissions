# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import DefaultDict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = DefaultDict(list)
        def dfs(root: Optional[TreeNode], col: int, row: int):
            if not root:
                return 
            cols[col].append((row, root.val))
            dfs(root.left, col - 1, row + 1)
            dfs(root.right, col + 1, row + 1) 

        dfs(root, 0, 0)

        res = []
        for col in sorted(cols):
            col_val = sorted(cols[col], key= lambda x: x[0])
            res.append([x for _, x in col_val])

        return res
 