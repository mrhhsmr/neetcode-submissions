class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        
        sides = [0] * 4
        length = sum(matchsticks) / 4
        matchsticks.sort(reverse=True)
    
        def dfs(index):
            if index == len(matchsticks):
                return True

            for side in range(4):
                if sides[side] + matchsticks[index] <= length:
                    sides[side] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sides[side] -= matchsticks[index]

                if sides[side] == 0:
                    break
        
            return False
        
        return dfs(0)
