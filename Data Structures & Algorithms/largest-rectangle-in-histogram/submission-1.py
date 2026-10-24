class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        res = 0
        h_l = len(heights)
        for i, h in enumerate(heights):
            if not stack or stack[-1][1] < h:
                stack.append([i+1,h])
            else:
                while(stack and stack[-1][1] >= h):
                    poped_index, poped_height = stack.pop()
                    area = (i - poped_index + 1) * poped_height
                    res = max(area, res)
                stack.append([poped_index,h])
        for ele in stack:
            area = (h_l - ele[0] + 1) * ele[1]
            res = max(area, res)
        return res
                     
        