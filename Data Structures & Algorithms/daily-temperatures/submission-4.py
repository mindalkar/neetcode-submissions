class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0] * len(temperatures)
        stack = [] # [index, value]
        for i, value in enumerate(temperatures):
            while(stack and stack[-1][1] < value):
                top = stack.pop()
                index = top[0]
                output[index] = i - index
            stack.append([i, value])
        
        return output



        