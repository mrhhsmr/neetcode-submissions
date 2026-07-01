class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        curr = []
        def dfs(curr):
            if len(curr) == len(nums):
                res.add(tuple(curr))
                return
            
            for i in range(len(nums)):
                if nums[i] != float("-inf"):
                    curr.append(nums[i])
                    nums[i] = float("-inf")
                    dfs(curr)
                    nums[i] = curr[-1]
                    curr.pop()

        dfs(curr)
        return list(res)