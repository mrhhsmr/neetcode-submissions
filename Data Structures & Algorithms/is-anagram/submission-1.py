class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = dict()
        mp2 = dict()
        for i in s:
            if i in mp1:
                val = mp1[i]
                mp1[i] = val + 1
            else:
                mp1[i] = 1
        
        for i in t:
            if i in mp2:
                val = mp2[i]
                mp2[i] = val + 1
            else:
                mp2[i] = 1

        return mp1 == mp2
        