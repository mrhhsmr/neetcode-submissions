class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(target, index):
            if target < 0:
                return
            
            if target == 0:
                res.append(cur.copy())
                return
            
            for i in range(index, len(nums), 1):
                cur.append(nums[i])
                dfs(target - nums[i], i)
                cur.pop()
        
        dfs(target, 0)
        return res