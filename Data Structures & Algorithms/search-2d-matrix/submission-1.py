class Solution:
    def check(self,lst:List[int],x:int,target:int)->bool:
        return lst[x]-target>0
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(0,m):
            lst.append(matrix[i][0])
        # print(lst)
        lo=0 
        hi=len(lst)-1
        if matrix[0][0]>target:
            return False
        ans=hi
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if lst[mid]==target:
                return True
            if self.check(lst,mid,target):
                hi=mid-1
            else:
                ans=mid
                lo=mid+1

        #now we have ans index which is the index of the row where we want to apply bs to look for target
        lst1=matrix[ans]
        lo1=0
        hi1=n-1
        ans1=0

        while(lo1<=hi1):
            mid1=lo1+(hi1-lo1)//2
            if target==lst1[mid1]:
                return True
            if self.check(lst1,mid1,target):
                hi1=mid1-1
            else:
                ans1=mid1
                lo1=mid1+1

        if lst1[ans1]==target:
            return True
        return False





        # return True
        