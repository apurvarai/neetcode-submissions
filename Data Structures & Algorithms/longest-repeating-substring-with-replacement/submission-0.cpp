class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_set<char> charset(s.begin(),s.end());
        int res=0;int n=s.length();
        for(auto c:charset){
int l=0;int cnt=0;
for(int r=l;r<n;r++){
    if(s[r]==c) cnt++;
    while((r-l+1)-cnt > k){
        if(s[l]==c) cnt--;
        l++;
    }
    res=max(res,r-l+1);
}
        }
        return res;

        
    }
};
