"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(root: 'Node', ans: List[int]) -> List[int]:
            if not root:
                return []
            for child in root.children:
                dfs(child, ans)
            ans.append(root.val)
            return ans
        return dfs(root, [])
        