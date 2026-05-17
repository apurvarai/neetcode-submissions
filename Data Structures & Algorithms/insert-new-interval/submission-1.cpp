class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int a,b;
        a=newInterval[0];b=newInterval[1];
        int n=intervals.size();vector<vector<int>> res;int i=0;
while(i<n && intervals[i][1]<a){
    res.push_back(intervals[i]);i++;
}
while(i<n && intervals[i][0]<=b){
    a=min(a,intervals[i][0]);//key step
    b=max(b,intervals[i][1]);//key step
    i++;
}
res.push_back({a,b});
while(i<n){
res.push_back(intervals[i]);i++;
}
return res;
    }
};
