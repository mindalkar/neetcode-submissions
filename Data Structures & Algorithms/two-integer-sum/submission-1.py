class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            first_num = nums[i]
            sec_num = target - first_num
            try:
                idx = nums.index(sec_num, i+1)
                return [i, idx]
            except ValueError:
                continue
        