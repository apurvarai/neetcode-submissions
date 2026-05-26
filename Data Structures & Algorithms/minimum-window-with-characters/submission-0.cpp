class Solution {
public:
    string minWindow(string s, string t) {
        int first;
        int last;
        for(int i=0;i<s.length();i++){
            if(s[i]==t[0]){
                first=i;break;
            }
        }
        for(int i=s.length()-1;i>=0;i--){
            if(s[i]==t[t.length()-1]){
                last=i;break;
            }
        }
        string c="";
        c+=s[first];
int i=first+1;int j=1;
while(i<=last && j<t.length()){
    if(s[i]!=t[j]){
        c+=s[i];i++;
    }
    else{
        c+=s[i];i++;j++;
    }
}
if(j<t.length()){
    return "";
}

    return c;



    }
};
