class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n=len(operations)
        i=0
        st=deque()
        while i<n:
            if operations[i]=="+":
                n1=st.pop()
                n2=st.pop()
                st.append(n2)
                st.append(n1)
                st.append(n1+n2)
            elif operations[i]=="C":
                st.pop()
            elif operations[i]=="D":
                n=st.pop()
                st.append(n)
                st.append(2*n)
            else:
                st.append(int(operations[i]))
            i+=1
        sum1=0
        print(st)
        while len(st):
            sum1+=st.pop()
        return sum1

        