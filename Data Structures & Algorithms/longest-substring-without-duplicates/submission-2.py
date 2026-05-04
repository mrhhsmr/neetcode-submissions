class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        l = 0
        r = 0
        res = 0
        while r < len(s):
            while l < r and s[r] in st:
                st.remove(s[l])
                l += 1

            st.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        
        return res
