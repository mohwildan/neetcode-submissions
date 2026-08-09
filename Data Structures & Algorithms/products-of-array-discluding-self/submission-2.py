class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # Product of everything to the left
        i = 0
        product = 1

        while i < len(nums):
            result[i] = product
            product *= nums[i]
            i += 1

        # Product of everything to the right
        i = len(nums) - 1
        product = 1

        while i >= 0:
            result[i] *= product
            product *= nums[i]
            i -= 1

        return result