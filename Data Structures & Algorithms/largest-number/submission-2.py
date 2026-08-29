class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        result = []

        while nums:
            best = max(nums, key=lambda x: x + max(nums))
            result.append(best)
            nums.remove(best)

        if result[0] == "0":
            return "0"

        return "".join(result)
