class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st =[]
        if len(tokens) > 1:
            for i in tokens:
                if i == '+':
                    add = int(st[-2]) + int(st[-1])
                    st.pop()
                    st.pop()
                    st.append(add)
                elif i == '-':
                    minn = int(st[-2]) - int(st[-1])
                    st.pop()
                    st.pop()
                    st.append(minn)
                elif i == '*':
                    mul = int(st[-2]) * int(st[-1])
                    st.pop()
                    st.pop()
                    st.append(mul)
                elif i == '/':
                    div = int(int(st[-2]) / int(st[-1]))
                    st.pop()
                    st.pop()
                    st.append(div)
                else:
                    st.append(i)
            return int(st[-1])
        else:
            return int(tokens[-1])