class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_dict = {}
        for item in nums:
            try:
                num_dict[item] += 1
            except KeyError:
                num_dict[item] = 1
        
        #print(num_dict)
        sorted_dict_desc = dict(sorted(num_dict.items(), key=lambda item: item[1], reverse=True))
        #print(sorted_dict_desc)
        #print(sorted_dict_desc.keys())
        return list(sorted_dict_desc.keys())[0:k]

        