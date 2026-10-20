class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]*len(height)
        maxRight = [0]*len(height)

        max_l = 0
        for i in range(1, len(height)):
            if height[i-1] > max_l:
                max_l = height[i-1]
            maxLeft[i] = max_l

        max_r = 0
        for i in range(len(height) - 2, 0, -1):
            if height[i+1] > max_r:
                max_r = height[i+1]
            maxRight[i] = max_r
        
        waterTrapped = 0

        #print(maxLeft)
        #print(maxRight)

        for i in range(0, len(height)):
            temp = min(maxLeft[i], maxRight[i]) - height[i]
            if temp < 0:
                temp = 0
            waterTrapped += temp
        
        return waterTrapped