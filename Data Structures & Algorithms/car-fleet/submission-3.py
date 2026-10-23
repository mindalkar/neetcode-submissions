class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair):
            t = (target - p)/s
            if not stack or stack[-1] > t:
                stack.append(t)
            else:
                while(stack and stack[-1]<=t):
                    stack.pop()
                stack.append(t)
        return len(stack)
        