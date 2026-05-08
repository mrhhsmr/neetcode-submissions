class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        maxFreq = 0
        res = 0
        l = 0
        r = 0
        while r < len(s):
            freq[ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, freq[ord(s[r]) - ord('A')])
            while r - l + 1 - maxFreq > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1

        return res