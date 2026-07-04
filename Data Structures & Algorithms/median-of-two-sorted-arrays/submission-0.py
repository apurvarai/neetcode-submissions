class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getk(A,B,k):
            if len(A)>len(B):
                A,B=B,A
            if not A:
                return B[k-1]
            if k==1:
                return min(A[0],B[0])
            i=min(len(A),k//2)
            j=min(len(B),k//2)
            if A[i-1]<B[j-1]:
                return getk(A[i:],B,k-i)
            else:
                return getk(A,B[j:],k-j)
        tot=len(nums1)+len(nums2)
        if tot%2:
            return getk(nums1,nums2,(tot+1)//2)
        else:
            return (getk(nums1,nums2,(tot//2+1))+getk(nums1,nums2,tot//2))/2
                
        