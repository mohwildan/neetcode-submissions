# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.pairs = []


        def dfs(root: Optional[TreeNode]):

            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            height = max(left, right) + 1

            self.pairs.append((height, root.val))

            return height

        dfs(root)
        self.pairs.sort(key= lambda x: (x[0]))

        count = {x[0] for x in self.pairs}

        ans = [[] for _ in range(len(count))] 

        for key, val in self.pairs:
            ans[key].append(val)

        return ans

 