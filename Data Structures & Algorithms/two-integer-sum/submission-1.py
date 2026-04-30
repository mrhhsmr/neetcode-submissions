class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()
        for i in range(len(nums)):
            if target - nums[i] in mp:
                return [mp.get(target - nums[i]), i]
            
            mp[nums[i]] = i;
        
        return []