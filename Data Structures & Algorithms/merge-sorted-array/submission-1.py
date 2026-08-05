class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while n > 0:
            nums1.pop()
            n -= 1

        for i in range(len(nums2)):
            nums1.append(nums2[i])

        for i in range(len(nums1)):
            j = i - 1

            while j >= 0 and nums1[j + 1] < nums1[j]:
                temp = nums1[j + 1]
                nums1[j + 1]  = nums1[j]
                nums1[j] = temp

                j -= 1

