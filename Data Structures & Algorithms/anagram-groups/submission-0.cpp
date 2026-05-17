class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> res;
    for(auto s : strs){
        string str=s;
        sort(str.begin(),str.end());
        res[str].push_back(s);
    }
    vector<vector<string>> result;
    for(auto i : res){
result.push_back(i.second);
    }
return result;
    }
};
