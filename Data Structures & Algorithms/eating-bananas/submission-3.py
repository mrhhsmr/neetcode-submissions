class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            
            # too slow, speeding up
            if hours > h:
                left = mid + 1
            else:
                right = mid
        
        return left