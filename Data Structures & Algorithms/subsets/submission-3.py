class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def dfs(index):
            res.append(cur.copy())
            if index >= len(nums):
                return 

            for i in range(index, len(nums), 1):
                cur.append(nums[i])
                dfs(i + 1)
                cur.pop()
        
        dfs(0)
        return res