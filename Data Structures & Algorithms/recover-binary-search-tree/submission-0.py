# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        def dfs(
            node: Optional[TreeNode],
            prev: Optional[TreeNode],
            first: Optional[TreeNode],
            second: Optional[TreeNode],
        ) -> tuple[
            Optional[TreeNode],
            Optional[TreeNode],
            Optional[TreeNode],
        ]:
            if not node:
                return prev, first, second

            prev, first, second = dfs(
                node.left,
                prev,
                first,
                second,
            )

            if prev and prev.val > node.val:
                if first is None:
                    first = prev

                second = node

            prev = node

            return dfs(
                node.right,
                prev,
                first,
                second,
            )

        _, first, second = dfs(
            root,
            None,
            None,
            None,
        )

        if first and second:
            first.val, second.val = second.val, first.val

        dfs(root, None, None, None)