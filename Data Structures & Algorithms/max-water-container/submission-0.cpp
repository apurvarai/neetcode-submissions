class Solution {
public:
    int maxArea(vector<int>& heights) {
        int res=0;
int n=heights.size();
        int i=0;int j=n-1;
        while(i<j){
            res=max(res,(j-i)*min(heights[i],heights[j]));
            if(heights[i]<heights[j]) i++;
            else j--;
        }
        return res;
        
    }
};
