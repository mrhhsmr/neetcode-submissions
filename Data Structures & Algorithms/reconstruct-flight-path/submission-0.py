class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        mp = {}
        tickets.sort()
        for src, dst in tickets:
            if src not in mp:
                mp[src] = []
            mp[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            if src not in mp:
                return False
            
            temp = list(mp[src])
            for i in range(len(temp)):
                nextAP = temp[i]
                mp[src].pop(i)
                res.append(nextAP)
                if dfs(nextAP):
                    return True
                
                mp[src].insert(i, nextAP)
                res.pop()
            
            return False
        
        dfs("JFK")
        return res
                
