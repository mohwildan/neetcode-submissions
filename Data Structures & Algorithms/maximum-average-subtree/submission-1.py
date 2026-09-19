
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]):
        
        m_ans = 0
        def dfs(root: Optional[TreeNode])-> tuple[int, int]:
            nonlocal m_ans
            if not root:
                return 0,0
            
            l_cal, l_c = dfs(root.left)
            r_cal, r_c = dfs(root.right)


            count = l_c + r_c + 1
            cals = (root.val + l_cal + r_cal)
            m_ans = max(m_ans, cals / count)
            return cals,count 

        _, _ = dfs(root)
        return m_ans