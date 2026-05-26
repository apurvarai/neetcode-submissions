class Solution {
public:
bool check(vector<int> &nums,int i){
    if(nums[i]-nums[0]>=0) return true;
return false;
}
    int search(vector<int>& nums, int target) {
        int n=nums.size();
        int low=0;
        int high=n-1;
        int ans=0;
        while(low<=high){
            int mid=low+(high-low)/2;
if(check(nums,mid)){
    low=mid+1;
}
else{
    ans=mid;
    high=mid-1;
}
        }

int pivot=ans;

if(nums[0]<=target){
    low=0;high=pivot-1;
}
else{
    low=pivot;high=n-1;
}

int final_ans=-1;
while(low<=high){
    int mid=low+(high-low)/2;
if(check(nums,mid)){
    low=mid+1;
}
else{
    final_ans=mid;
    high=mid-1;
}
}
if(nums[final_ans]==target)
return final_ans;
else return -1;
    }
};
