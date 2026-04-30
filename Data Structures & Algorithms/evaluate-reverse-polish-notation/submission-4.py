class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = list()
        for token in tokens:
            try:
                num = int(token)
            except  ValueError:
                num1 = st.pop()
                num2 = st.pop()
                if token == "+":
                    num = num1 + num2
                elif token == "-":
                    num = num2 - num1
                elif token == "*":
                    num = num1 * num2
                else:
                    num = int(num2 / num1)
            finally:
                st.append(num)
        
        return int(st[0])