class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        st = set()
        i = 0
        j = 0
        while j < len(nums):
            if j - i > k:
                st.remove(nums[i])
                i += 1

            if nums[j] in st:
                return True
            
            st.add(nums[j])
            j += 1

        
        return False
