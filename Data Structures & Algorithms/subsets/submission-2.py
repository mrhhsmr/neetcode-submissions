class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        i = 0 
        def dfs(index):
            res.append(curr.copy())
            if index == len(nums):
                return
            
            for i in range(index, len(nums), 1):
                curr.append(nums[i])
                dfs(i + 1)
                curr.pop() 

        dfs(0)
        return res