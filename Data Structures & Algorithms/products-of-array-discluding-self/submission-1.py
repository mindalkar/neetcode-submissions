class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a_len = len(nums)
        pre_arr = [None] * a_len
        suf_arr = [None] * a_len
        out_arr = [None] * a_len
        pre_arr[1] = nums[0]
        #[None, 1, None, None]

        suf_arr[a_len - 2] = nums[a_len - 1]

        for i in range(2, a_len):
            pre_product = nums[i-1] * pre_arr[i-1]
            pre_arr[i] = pre_product
            #[None, 1, 2, 8]
        #print(pre_arr)
        
        
        for i in range(a_len - 3, -1, -1):
            #print(i)
            suf_product = nums[i+1] * suf_arr[i+1]
            suf_arr[i] = suf_product
            #[None, 1, 2, 8]
        #print(suf_arr)

        for i in range(0, a_len):
            if pre_arr[i] is None:
                out_arr[i] = suf_arr[i]
            elif suf_arr[i] is None:
                out_arr[i] = pre_arr[i]
            else:
                out_arr[i] = pre_arr[i] * suf_arr[i]
        
        return out_arr


        