class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for b in s:
            if b in ["(", "{", "["]:
                stack.append(b)
            elif b in [")", "}", "]"]:
                if not stack:
                    return False
                upperElement = stack.pop()
                if b == ")" and upperElement != "(":
                    return False
                elif b == "}" and upperElement != "{":
                    return False
                elif b == "]" and upperElement != "[":
                    return False
        
        if stack:
            return False
        return True
        