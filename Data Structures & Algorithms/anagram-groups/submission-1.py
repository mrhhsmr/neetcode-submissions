class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = dict()
        for str1 in strs:
            counts = [0] * 26
            for i in str1:
                 counts[ord(i) - ord("a")] += 1
            
            if tuple(counts) not in mp:
                mp[tuple(counts)] = []
            mp[tuple(counts)].append(str1)
            
        return list(mp.values());