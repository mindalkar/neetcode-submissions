class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0

        for n in numSet:
            if (n - 1) not in numSet:
                l_seq = 1
                while (n+1) in numSet:
                    l_seq += 1
                    n += 1
                if l_seq > longestSeq:
                    longestSeq = l_seq
        return longestSeq
            