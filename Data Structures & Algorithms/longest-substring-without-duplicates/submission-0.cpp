class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res=0;

        unordered_set<char> charset;
int n=s.length();
int l=0;
        for(int r=0;r<n;r++){
            while(charset.find(s[r])!=charset.end()){
                charset.erase(s[l]);l++;
            }
charset.insert(s[r]);
res=max(res,(int)charset.size());

        }
        return res;
        
    }
};
