class Solution:
    def countElements(self, arr: List[int]) -> int:

        count = 0

        i = 0
        while i < len(arr):
            if (arr[i] + 1) in arr:
                count += 1
            i += 1
        
        return count