class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ##we keep 3 variables to store current count of 5,10,20 notes
        # for 10, cnt2>0 : for 20, cnt2>0 and cnt3>0
        n=len(bills)
        cnt1,cnt2,cnt3=0,0,0
        for i in bills:
            if i==5:
                cnt1+=1
            elif i==10:
                cnt2+=1
                if cnt1<=0:
                    return False
                else:
                    cnt1-=1
            else:
                cnt3+=1
                if cnt2<=0 or cnt1<=0:
                    return False
                else:
                    cnt1-=1
                    cnt2-=1
        return True
        