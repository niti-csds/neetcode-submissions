class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for c in tokens:
            if c not in ['+', '-', '*', '/']:
                st.append(int(c))
            else:
                op2 = st.pop()
                op1 = st.pop()
                if c == '+':
                    st.append(op1 + op2)
                elif c == '-':
                    st.append(op1 - op2)
                elif c == '*':
                    st.append(op1*op2)
                else:                 
                    st.append(int(op1/op2))
        return st[0] if st else None