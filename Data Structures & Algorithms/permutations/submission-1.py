class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return;

            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i]);
                    dfs()
                    curr.pop()
        
        dfs()
        return res
            
