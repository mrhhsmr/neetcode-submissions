class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = 0
        mp = [0] * 26
        maxFreq = 0
        while r < len(s):
            mp[ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, mp[ord(s[r]) - ord('A')])
            while r - l + 1 - maxFreq > k:
                 mp[ord(s[l]) - ord('A')] -= 1
                 l += 1
            
            res = max(res, r - l + 1)
            r += 1

        return res
