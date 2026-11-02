class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        elif s1 == s2 :
            return True
        elif len(s1) == 1 and len(s2) != 1:
            return True
        l, r = 0, len(s1)
        sorted_s1 = "".join(sorted(s1))
        hash_s1 = {}
        hash_s2 = {}
        
        i = 0
        for i in range(len(s1)):
            try:
                hash_s1[s1[i]] += 1
            except KeyError:
                hash_s1[s1[i]] = 1

            try:
                hash_s2[s2[i]] += 1
            except KeyError:
                hash_s2[s2[i]] = 1



        while (r<=len(s2)):
            all_match = True
            for key in hash_s1:
                if key not in hash_s2 or hash_s1[key] != hash_s2[key]:
                    all_match = False
                    break
            if all_match:
                return True
            elif r == len(s2):
                break
            else:
                hash_s2[s2[l]] -= 1
                try:
                    hash_s2[s2[r]] += 1
                except KeyError:
                    hash_s2[s2[r]] = 1
                l += 1
                r += 1




            # sub_s = s2[l:r+1]
            # if "".join(sorted(sub_s)) == sorted_s1:
            #     return True
            # l += 1
            # r += 1
        
        return False

        