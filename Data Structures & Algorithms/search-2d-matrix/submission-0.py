class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            nums = matrix[i]
            if nums[-1] < target:
                continue
            for value in nums:
                if value == target:
                    return True
        return False
