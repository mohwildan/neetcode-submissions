class Solution:

    def encode(self, strs: List[str]) -> str:
        endcode_chunk = ""

        for v in strs:
            endcode_chunk += f"{v}*#" 
        
        return endcode_chunk

    def decode(self, s: str) -> List[str]:
        result = []
        str_arr = []

        j = 0
        while j < len(s):
            print(s[j:j+2])
            if s[j:j+2] == "*#":
                str_arr.append("*#")
                j += 2
            else:
                str_arr.append(s[j])
                j += 1

        i = 0
        tmp = ""
        while i < len(str_arr):
            data = str_arr[i]
            if data != "*#":
                tmp += data
            else:
                result.append(tmp)
                tmp = ""

            i += 1

        return result

