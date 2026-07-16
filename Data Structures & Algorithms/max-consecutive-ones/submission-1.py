class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        current_consecutive_one = 0
        max_consecutive_one = 0
        for n in nums:
            current_consecutive_one += 1
            if n == 1:
                if current_consecutive_one > max_consecutive_one:
                    max_consecutive_one = current_consecutive_one
            else:
                current_consecutive_one = 0
        return max_consecutive_one
        