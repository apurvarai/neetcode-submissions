class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]#[temp,index]
        out=[0]*len(temperatures)
        for i,tmp in enumerate(temperatures):
            while st and tmp>st[-1][0]:
                c=st.pop()
                out[c[1]]=(i-c[1])
            st.append([tmp,i])
        while st:
            c=st.pop()
            out[c[1]]=0
        return out
                
        