class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        if sum(nums)>=target:
            win=n
        else:
            return 0
        i,j=0,0
        curr=0
        while j<n:
            if curr<target:
                # j+=1
                curr+=nums[j]
                print(curr,"!")
                j+=1
                # if curr>=target:
                #     win=min(win,j-i+1)
            else:
                # j+=1
                win=min(win,j-i)
                while i<j and curr>=target:
                    curr-=nums[i]
                    print(curr,";")
                    i+=1
                    print(i)
                    # print(curr)
                    if curr>=target:
                        win=min(win,j-i)
                # j+=1
            # print(i)
        while i<n and curr>=target:
            win=min(win,j-i)
            curr-=nums[i]
            i+=1
        return win
                    

        