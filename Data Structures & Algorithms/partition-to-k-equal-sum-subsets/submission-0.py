class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sumK = sum(nums)
        if sumK % k != 0:
            return False

        sumK //= k
        used = [False] * len(nums)
        def dfs(i, k, curSum):
            if k == 0:
                return True
            
            if curSum == sumK:
                return dfs(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or nums[j] + curSum > sumK:
                    continue
                used[j] = True
                if dfs(j + 1, k, nums[j] + curSum):
                    return True
                used[j] = False
            
            return False
            
        return dfs(0, k, 0)