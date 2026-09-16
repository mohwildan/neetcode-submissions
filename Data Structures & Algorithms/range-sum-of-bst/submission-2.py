# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:

        def dfs(root: TreeNode | None, res: List):
            if not root:
                return
            res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)

            return res

        dfs_arr = sorted(dfs(root, []) or [])

        sum_cal = 0
        for x in dfs_arr:
            if x <= high and x >= low:
                sum_cal += x
        return sum(x for x in dfs_arr if x >= low and x <= high)
 