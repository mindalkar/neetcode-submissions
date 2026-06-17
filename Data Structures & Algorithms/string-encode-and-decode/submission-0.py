import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            s_len = len(s)
            reversed_text = s[::-1]
            ret = f"{ret}#{s_len}#{reversed_text}"
        return ret

    def decode(self, s: str) -> List[str]:
        ret_list = []
        parts = re.split(r'#\d+#', s)
        for s in parts[1:]:
            reversed_text = s[::-1]
            ret_list.append(reversed_text)
        return ret_list

        

        
