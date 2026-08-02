class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        uniq=set(s)
        arr=[]
        for ch in uniq:
            arr.append([s.find(ch),s.rfind(ch)])
        #Run merge overlapping intervals over arr
        arr.sort()
        print(arr)
        curr=arr[0]
        res=[]
        for i in range(1,len(arr)):
            if curr[1]<arr[i][0]:
                res.append(curr.copy())
                curr=arr[i]
            else:
                curr=[curr[0],max(curr[1],arr[i][1])]
        res.append(curr)
        print(res)
        cnt=[0]*len(res)
        for i,j in enumerate(res):
            cnt[i]=(1+j[1]-j[0])
        return cnt



        