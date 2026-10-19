class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_i = 0
        

        s_without_space = s.replace(" ", "").lower()
        result = "".join(char for char in s_without_space if char.isalnum())
        r_i = len(result) - 1
        while (l_i<=r_i):
            if result[l_i] != result[r_i]:
                return False
            l_i += 1
            r_i -= 1
        return True
            

        