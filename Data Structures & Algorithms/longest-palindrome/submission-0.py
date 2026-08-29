class Solution:
    def longestPalindrome(self, s: str) -> int:

        count = defaultdict(int)  
        res = 0

        for c in s:
           count[c] += 1

           if not count[c] % 2:
               res += 2
        
        for cnt in count.values():
            if cnt % 2:
                res += 1
                break

        return res
