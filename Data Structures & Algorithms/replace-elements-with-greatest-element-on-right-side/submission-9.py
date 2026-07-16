class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arrs = []
        for i,_ in enumerate(arr):
            if not i + 1 >= len(arr):
                arrs.append(max(arr[i + 1:]))
        arrs.append(-1)
        return arrs

        