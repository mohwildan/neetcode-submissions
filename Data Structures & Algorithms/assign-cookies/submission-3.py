class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        i, j = 0, 0

        has_content = 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                has_content += 1
                i += 1
            j += 1
        return has_content
