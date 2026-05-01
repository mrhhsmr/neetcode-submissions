class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = dict()
        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1;
        
        arr = []
        for num, cnt in hmap.items():
            arr.append([cnt, num])
        
        arr.sort()
        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res

        