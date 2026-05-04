class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {0 : 1}
        def dfs(total):
            if total in memo:
                return memo[total]
                
            if total == 0:
                return 1

            res = 0
            for i in range(len(nums)):
                if total < nums[i]:
                    break
                res += dfs(total - nums[i])
            memo[total] = res
            return res

        return dfs(target)