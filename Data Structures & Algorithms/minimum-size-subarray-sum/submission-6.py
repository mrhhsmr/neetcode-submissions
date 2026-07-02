class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf') 
        i, j = 0, 0
        curr = 0
        while j < len(nums):
            curr += nums[j]
            while i <= j and curr >= target:
                minlen = min(minlen, j - i + 1)
                curr -= nums[i]
                i += 1
            j += 1
        
        return 0 if minlen == float("inf") else minlen