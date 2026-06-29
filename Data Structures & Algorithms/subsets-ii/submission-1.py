class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []
        def dfs(index):
            res.append(cur.copy())
            if index == len(nums):
                return 
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                
                cur.append(nums[i])
                dfs(i + 1)
                cur.pop()
        
        dfs(0)
        return res