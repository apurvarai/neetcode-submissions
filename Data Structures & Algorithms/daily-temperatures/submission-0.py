class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output=[0]*len(temperatures)
        for i,tmp in enumerate(temperatures):
            while stack and tmp>stack[-1][0]:
                c=stack[-1]
                stack.pop()
                output[c[1]]=(i-c[1])
            stack.append([tmp,i])
        return output
        