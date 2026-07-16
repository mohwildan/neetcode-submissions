class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element = -1
        for i in range(len(arr) - 1, -1, -1):
            real_element = arr[i]

            arr[i] = max_element

            if real_element > max_element:
                max_element = real_element
        return arr

            