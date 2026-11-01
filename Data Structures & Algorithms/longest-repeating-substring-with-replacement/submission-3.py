class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        charHash = {s[l]: 1}
        res = 1
        if len(s) == 1:
            return res
        while (r<len(s)):
            win_len = r - l + 1
            try:
                charHash[s[r]] += 1
            except KeyError:
                charHash[s[r]] = 1
            maxCount = 0
            for c in charHash:
                maxCount = max(maxCount, charHash[c])
            if win_len - maxCount <= k:
                res = max(res, win_len)
            else:
                charHash[s[l]] -= 1
                l += 1
            r += 1
        return res
                
        