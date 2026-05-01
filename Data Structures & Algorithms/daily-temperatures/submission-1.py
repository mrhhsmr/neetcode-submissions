class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = list() # ([temp, index])
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while st and st[-1][0] < temp:
                stTemp, stInd = st.pop()
                res[stInd] = i - stInd
            st.append([temp, i])
        
        return res
            
        