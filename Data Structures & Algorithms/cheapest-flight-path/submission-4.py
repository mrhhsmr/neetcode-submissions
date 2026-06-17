class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mp = {}
        for source, dest, price in flights:
            if source not in mp:
                mp[source] = []
            
            mp[source].append([dest, price])
        
        pq = [(0, src, k + 1)] # cost, city, stops
        best_stops = {src: k + 1}
        while pq:
            cost, currCity, stops = heapq.heappop(pq)
            if currCity == dst:
                return cost
            
            if stops > 0:
                nextCities = mp.get(currCity, [])
                if len(nextCities) == 0:
                    continue
                
                if stops < best_stops.get(currCity, -1):
                    continue
                
                best_stops[currCity] = stops
                
                for nextCity, price in nextCities:
                    heapq.heappush(pq, (cost + price, nextCity, stops - 1))
        
        return -1
        

        