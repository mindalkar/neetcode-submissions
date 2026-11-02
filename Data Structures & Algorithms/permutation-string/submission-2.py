class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        l, r = 0, len(s1) - 1
        sorted_s1 = "".join(sorted(s1))
        while (r<len(s2)):
            sub_s = s2[l:r+1]
            if "".join(sorted(sub_s)) == sorted_s1:
                return True
            l += 1
            r += 1
        
        return False

        