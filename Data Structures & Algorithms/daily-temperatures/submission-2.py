class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0] * len(temperatures)
        stack = [] # [index, value]
        for i in range(0, len(temperatures)):
            while(stack and stack[-1][1] < temperatures[i]):
                top = stack.pop()
                output[top[0]] = i - top[0]
            stack.append([i, temperatures[i]])
        
        return output



        