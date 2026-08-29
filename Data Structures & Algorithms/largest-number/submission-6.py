class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        ns: List[str] = [str(n) for n in nums]


        i = 0

        while i < len(ns):
            j = 0
            while j < len(ns) - 1:
                if (ns[j] + ns[j + 1]) < (ns[j + 1] + ns[j]):
                    temp = ns[j]
                    ns[j] = ns[j + 1]
                    ns[j + 1] = temp
                j += 1
            i += 1

        if ns[0] == "0":
            return "0"

        return "".join(ns)

