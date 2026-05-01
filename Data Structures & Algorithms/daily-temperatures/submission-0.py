class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = list() # [temp, index]
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while st and t > st[-1][0]:
                stTemp, stIndex = st.pop()
                res[stIndex] = i - stIndex 
            st.append([t, i])
        
        return res

            
        