class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        dp = []

        i = 0
        while i < numRows:
            row = [1] * (i + 1)

            j = 1
            while j < i:
                row[j] = dp[i - 1][j - 1] + dp[i - 1][j]
                j += 1
            dp.append(row)

            i += 1



        return dp
