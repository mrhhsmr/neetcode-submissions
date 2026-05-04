class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        res = float("inf")
        curr = 0
        while r < len(nums):
            curr += nums[r]
            while l <= r and curr >= target:
                res = min(res, r - l + 1)
                curr -= nums[l]
                l += 1
            r += 1
        
        return 0 if res == float("inf") else res
