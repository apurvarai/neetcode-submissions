bool cmp(pair<int,int>& a,pair<int,int>& b) 
       { return a.second<b.second;}
void sort(map<int,int> &mp){
    vector<pair<int,int>> A;
    for(auto it:mp) A.push_back(it);
    sort(A.begin(),A.end(),cmp);
}
class Solution {
// bool cmp(pair<int,int>& a,pair<int,int>& b) 
//        { return a.second>b.second;}
public:

// bool cmp(pair<int,int>& a,pair<int,int>& b) 
//        { return a.second>b.second;}

vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result;
map<int,int> mp1;
for(int i=0;i<nums.size();i++) mp1[nums[i]]++;
sort(mp1);


for(auto i:mp1){
    cout<<i.first<<" "<<i.second<<"\n";;
}

// map<int,int> mp2;
// for(auto i:mp1){
//     mp2[i.second]=i.first;
// }
// // for(auto i:mp2){
// //     cout<<i.first<<" "<<i.second<<"\n";;
// // }
// for (auto i:mp1){
//     if(k--)
//     result.push_back(i.first);
//     else break;
// }
auto it=mp1.end();
it--;

while(k--){
    result.push_back(it->first);
    it--;
}
return result;

        
    }
};
