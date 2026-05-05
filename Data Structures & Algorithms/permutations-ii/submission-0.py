class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        st = set()
        cur = []
        nums.sort()
        def dfs(cur):
            if len(cur) == len(nums):
                st.add(tuple(cur))
                return
            
            for i in range(len(nums)):
                if nums[i] != float("-inf"):
                    cur.append(nums[i])
                    nums[i] = float("-inf")
                    dfs(cur)
                    nums[i] = cur[-1]
                    cur.pop()
        
        dfs(cur)
        return list(st)