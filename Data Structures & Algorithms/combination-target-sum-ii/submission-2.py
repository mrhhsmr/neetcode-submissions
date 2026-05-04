class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()
        def dfs(target, index):
            if target < 0:
                return 
            
            if target == 0:
                res.append(cur.copy())
                return
            
            for i in range(index, len(candidates)):
                #如果当前数字和前一个数字一样，并且它不是这一层的第一个选择，就跳过
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                cur.append(candidates[i])
                dfs(target - candidates[i], i + 1)
                cur.pop()
        
        dfs(target, 0)
        return res
