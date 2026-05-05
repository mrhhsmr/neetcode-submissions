class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        st = set()
        cur = []
        nums.sort()
        visit = [0] * len(nums)
        def dfs(cur):
            if len(cur) == len(nums):
                st.add(tuple(cur))
                return
            
            for i in range(len(nums)):
                if visit[i] != 1:
                    cur.append(nums[i])
                    visit[i] = 1
                    dfs(cur)
                    visit[i] = 0
                    cur.pop()
        
        dfs(cur)
        return list(st)