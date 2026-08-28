class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        i = 0
        dp = []
        while i <= rowIndex:
            row = [1] * (i + 1)

            j = 1
            while j < i:
                row[j] = dp[i - 1][j - 1] + dp[i - 1][j]
                j += 1

            dp.append(row)
                
            i += 1
        return dp[rowIndex]
