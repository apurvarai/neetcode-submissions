class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result;
map<int,int> mp1;
for(int i=0;i<nums.size();i++) mp1[nums[i]]++;
map<int,int> mp2;
for(auto i:mp1){
    mp2[i.second]=i.first;
}
auto it=mp2.end();
it--;

while(k--){
    result.push_back(it->second);
    it--;
}
return result;

        
    }
};
