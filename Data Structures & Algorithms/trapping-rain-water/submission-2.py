class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = height[0]
        rightMax[n - 1] = height[n - 1]
        for i in range(0 , n, 1):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        for j in range(n - 2, -1, -1):
            rightMax[j] = max(rightMax[j + 1], height[j])
        
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        
        return res

        