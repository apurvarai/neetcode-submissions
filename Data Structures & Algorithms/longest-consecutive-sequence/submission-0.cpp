class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int result=0;
        unordered_set<int> numset(nums.begin(),nums.end());
        for(auto s:numset){
            if(numset.find(s-1)==numset.end()){
                int length=1;
                while(numset.find(s+length)!=numset.end()){
                    length+=1;
                }
                result=max(result,length);
            }
        }
        return result;
    }
};
