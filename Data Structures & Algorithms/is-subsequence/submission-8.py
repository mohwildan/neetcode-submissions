class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        m = len(s)
        n = len(t)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[0][j] = True


        i = 1
        while i <= m:
            j = 1

            while j <= n :

                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

                j += 1
            i += 1


        return dp[m][n]
