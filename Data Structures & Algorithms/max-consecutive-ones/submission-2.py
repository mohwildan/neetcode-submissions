class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_one = 0
        current_consecutive_one = 0
        
        for n in nums:
            if n == 1:
                current_consecutive_one += 1
                if current_consecutive_one > max_consecutive_one:
                    max_consecutive_one = current_consecutive_one
            else:
                current_consecutive_one = 0
        return max_consecutive_one

