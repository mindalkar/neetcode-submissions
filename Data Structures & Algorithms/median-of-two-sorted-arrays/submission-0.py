class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result_arr = []
        i = j = 0
        nums1_l, nums2_l = len(nums1), len(nums2)

        while (i< nums1_l or j < nums2_l):
            if i< nums1_l and j < nums2_l and nums1[i] <= nums2[j]:
                result_arr.append(nums1[i])
                i += 1
            elif i< nums1_l and j < nums2_l and nums1[i] > nums2[j]:
                result_arr.append(nums2[j])
                j += 1
            elif i< nums1_l:
                result_arr.append(nums1[i])
                i += 1
            elif j< nums2_l:
                result_arr.append(nums2[j])
                j += 1
        
        res_arr_len = len(result_arr)
        if res_arr_len % 2 == 1:
            return result_arr[res_arr_len//2]
        else:
            return float((result_arr[res_arr_len//2 - 1] + result_arr[res_arr_len//2])/2)
            