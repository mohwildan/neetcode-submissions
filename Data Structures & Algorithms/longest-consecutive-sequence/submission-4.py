class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        current = 1 
        longest = 1
        nums = sorted(nums)
        i = 0
        if len(nums) == 0:
            return 0

        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                pass
            
            elif nums[i] + 1 == nums[i + 1]:
                current += 1
            else:
                current = 1

            if current > longest:
                longest = current
            i += 1

        return longest
