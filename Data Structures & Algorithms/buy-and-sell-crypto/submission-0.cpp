class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n=prices.size();
        if(n==1) return 0;
        int i=0; int j=1;int profit=0;
        while(j<n){
            if(prices[i]<prices[j]){
            profit=max(profit,prices[j]-prices[i]);j++;}
            else{
                i=j;j=i+1;
            }
        }
        return profit;
        
    }
};
