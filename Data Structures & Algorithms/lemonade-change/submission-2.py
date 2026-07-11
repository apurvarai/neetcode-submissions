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
                    print(i,cnt1,cnt2,cnt3)
                    return False
                else:
                    cnt1-=1
            else:
                cnt3+=1
                #to return 15, we have 2 ways, 10+5 or 5+5+5
                if (cnt1<=2) and (cnt2<=0 or cnt1<=0):
                    return False
                else:
                    if cnt1>=0 and cnt2>=0:
                        cnt1-=1
                        cnt2-=1
                    else:
                        cnt1-=3

                # if cnt2<=0 or cnt1<=0:
                #     print(i,cnt1,cnt2,cnt3)
                #     return False
                # else:
                #     cnt1-=1
                #     cnt2-=1
        return True
        