class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_s_hash = {}
        char_t_hash = {}
        for i in range (len(s)):
            try:
                char_s_hash[s[i]] += 1
            except KeyError:
                char_s_hash[s[i]] = 1
            try:
                char_t_hash[t[i]] += 1
            except KeyError:
                char_t_hash[t[i]] = 1
        

        for key in char_s_hash:
            try:
                if char_s_hash[key] != char_t_hash[key]:
                    return False
            except KeyError:
                return False
        

        return True
        