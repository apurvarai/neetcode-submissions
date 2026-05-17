class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int a,b;map<int,int>mp;
        for(int i=0;i<nums.size();i++){
mp[nums[i]]=i;
        }
        for(int i=0;i<nums.size();i++){
        if(mp.find(target-nums[i])!=mp.end() && i!=mp.find(target-nums[i])->second){
            a=i;
            b=mp.find(target-nums[i])->second;
            break;
        }
        }
vector<int> v;
v.push_back(a);v.push_back(b);
        return v;
    }
};
