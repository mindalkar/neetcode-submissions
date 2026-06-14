class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_dict = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            try:
                dict_dict[sorted_s].append(s)
            except KeyError:
                dict_dict[sorted_s] = [s]
        
        ret = []
        for item in dict_dict:
            ret.append(dict_dict[item])
        return ret
        