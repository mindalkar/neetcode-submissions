class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        li = 0
        ri = len(numbers) - 1

        while(li<ri):
            sum_of_nums = numbers[li] + numbers[ri]
            if (sum_of_nums == target):
                return [li+1, ri+1]
            if sum_of_nums < target:
                li += 1
            if sum_of_nums > target:
                ri -= 1
            

        