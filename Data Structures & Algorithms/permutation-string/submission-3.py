class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        mp = [0] * 26
        for i in s1:
            mp[ord(i) - ord('a')] += 1

        curr = [0] * 26
        i, j = 0, 0
        while j < len(s1):
            curr[ord(s2[j]) - ord('a')] += 1
            j += 1
        
        while j < len(s2) and i < len(s2):
            if mp == curr:
                return True

            curr[ord(s2[i]) - ord('a')] -= 1
            curr[ord(s2[j]) - ord('a')] += 1
            i += 1
            j += 1
        
        if mp == curr:
            return True

        return False